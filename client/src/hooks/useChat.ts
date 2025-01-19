import { useState, useEffect } from 'react';
import { 
    Message, 
    ChatContext, 
    MessageAttachment, 
    ThreadCreatedPayload,
    MessageReceivedPayload,
    ImageReceivedPayload,
} from '../types';
import io from 'socket.io-client';

const socket = io('http://localhost:5001');

export function useChat() {
    const [context, setContext] = useState<ChatContext>({ messages: [] });
    const [threadId, setThreadId] = useState<string | null>(null);
    const [isTyping, setIsTyping] = useState(false);
    const [images, setImages] = useState<MessageAttachment[]>([]);
    const [isImageCarouselOpen, setIsImageCarouselOpen] = useState(false);

    useEffect(() => {
        socket.on('thread_created', (data: ThreadCreatedPayload) => {
            setThreadId(data.thread_id);
            socket.emit('join_thread', { thread_id: data.thread_id });
            if (context.csvContent) {
                setIsTyping(true); // Set typing when sending CSV
                socket.emit('send_csv', { thread_id: data.thread_id, csvContent: context.csvContent });
            }
        });

        socket.on('csv_processed', () => {
            // Keep typing true as the assistant will be generating initial response
            setIsTyping(true);
        });

        socket.on('message_received', (data: MessageReceivedPayload) => {
            console.log('Received messages:', data);
            if (data.messages.length !== 2) {
                data.messages.reverse();
            }
            setContext(prev => {
                // Get all existing messages that aren't in the new message set
                const existingMessages = prev.messages.filter(msg =>
                    !data.messages.some(newMsg =>
                        newMsg.content === msg.content && newMsg.role === msg.role
                    )
                );

                // Add new messages in reverse order (newest first)
                const newMessages = data.messages.reverse();

                return {
                    ...prev,
                    messages: [...existingMessages, ...newMessages]
                };
            });
            setIsTyping(false);
        });

        socket.on('message_sent', () => {
            setIsTyping(true);
        });

        socket.on('image_received', (data: ImageReceivedPayload) => {
            const newImage: MessageAttachment = {
                url: `data:image/png;base64,${data.image_data}`,
                type: 'image'
            };
            setImages(prev => [...prev, newImage]);

        });

        socket.on('thread_cleared', () => {
            setContext(prev => ({
                ...prev,
                messages: []
            }));
            setIsTyping(false);
        });

        return () => {
            socket.off('thread_created');
            socket.off('message_received');
            socket.off('image_received');
            socket.off('message_sent');
            socket.off('thread_cleared');
            socket.off('csv_processed');
        };
    }, [context.csvContent]);

    const handleFileAnalysis = (content: string) => {
        // Clear existing messages and images
        setContext({
            messages: [],
            csvContent: content
        });
        setImages([]); // Reset images array
        
        // Clear existing thread and create new one
        if (threadId) {
            socket.emit('clear_thread', { thread_id: threadId });
        }
        socket.emit('create_thread');
    };

    const handleSendMessage = async (content: string) => {
        if (!threadId) return;

        const userMessage: Message = {
            role: 'user',
            content,
            timestamp: new Date()
        };

        setContext(prev => ({
            ...prev,
            messages: [...prev.messages, userMessage]
        }));

        socket.emit('send_message', {
            thread_id: threadId,
            message: content
        });
    };

    const clearContext = () => {
        if (!threadId) return;
        
        // Preserve CSV content while clearing messages
        const csvContent = context.csvContent;
        setContext({ messages: [], csvContent });
        setImages([]); // Reset images array
        
        // Emit clear event to server
        socket.emit('clear_thread', { thread_id: threadId });
        
        // Create new thread for fresh conversation
        socket.emit('create_thread');
    };

    return {
        context,
        handleSendMessage,
        handleFileAnalysis,
        clearContext,
        isTyping,
        images,
        isImageCarouselOpen,
        setIsImageCarouselOpen
    };
}

import { useState, useEffect } from 'react';
import { Message, ChatContext } from '../types';
import { io } from 'socket.io-client';

const socket = io('http://localhost:5001');

export function useChat() {
    const [context, setContext] = useState<ChatContext>({ messages: []});
    const [threadId, setThreadId] = useState<string | null>(null);
    const [isTyping, setIsTyping] = useState(false);

    useEffect(() => {
        socket.on('thread_created', (data) => {
            setThreadId(data.thread_id);
            socket.emit('join_thread', { thread_id: data.thread_id });
            if (context.csvContent) {
                setIsTyping(true); // Set typing when sending CSV
                socket.emit('send_csv', { thread_id: data.thread_id, csvContent: context.csvContent});
            }
        });

        socket.on('csv_processed', () => {
            // Keep typing true as the assistant will be generating initial response
            setIsTyping(true);
        });

        socket.on('message_received', (data) => {
            console.log(data);
            // Ensure messages are stored in chronological order
            const reversedMessages = data.messages.reverse();
            setContext(prev => ({
                ...prev,
                messages: reversedMessages
            }));
            setIsTyping(false);
        });

        socket.on('message_sent', () => {
            setIsTyping(true);
        });

        socket.on('thread_cleared', (data) => {
            setContext(prev => ({
                ...prev,
                messages: []
            }));
            setIsTyping(false);
        });

        return () => {
            socket.off('thread_created');
            socket.off('message_received');
            socket.off('message_sent');
            socket.off('thread_cleared');
            socket.off('csv_processed');
        };
    }, [context.csvContent]);

    const handleFileAnalysis = (content: string) => {
        // Request new thread when file is uploaded
        setContext(prev => ({
            ...prev,
            csvContent: content
        }));    
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
        socket.emit('clear_thread', { thread_id: threadId });
    };

    return {
        context,
        handleSendMessage,
        handleFileAnalysis,
        clearContext,
        isTyping
    };
}

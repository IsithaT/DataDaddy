import { useState, useEffect } from 'react';
import { Message, ChatContext } from '../types';
import { io } from 'socket.io-client';

const socket = io('http://localhost:5001');

export function useChat() {
    const [context, setContext] = useState<ChatContext>({ messages: []});
    const [threadId, setThreadId] = useState<string | null>(null);

    useEffect(() => {
        socket.on('thread_created', (data) => {
            setThreadId(data.thread_id);
            socket.emit('join_thread', { thread_id: data.thread_id });
            console.log(context.csvContent?.toString());
            if (context.csvContent) {
                socket.emit('send_csv', { thread_id: data.thread_id, csvContent: context.csvContent});
            }
        });

        socket.on('message_received', (data) => {
            console.log(data);
            setContext(prev => ({
                ...prev,
                messages: data.messages
            }));
        });

        socket.on('image_received', (data) => {
            const imageMessage: Message = {
                role: 'assistant',
                content: 'Sent an image',
                timestamp: new Date(),
                attachments: [{
                    url: `data:image/png;base64,${data.image_data}`,
                    caption: 'Generated image',
                    type: 'image'
                }]
            };
            setContext(prev => ({
                ...prev,
                messages: [...prev.messages, imageMessage]
            }));
        });

        socket.on('thread_cleared', (data) => {
            setContext(prev => ({
                ...prev,
                messages: []
            }));
        });

        return () => {
            socket.off('thread_created');
            socket.off('message_received');
            socket.off('image_received');
            socket.off('thread_cleared');
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
        clearContext
    };
}

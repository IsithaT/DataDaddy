import { useState, useEffect } from 'react';
import { Message, ChatContext } from '../types';
import { io } from 'socket.io-client';

const socket = io('http://localhost:5001');

export function useChat() {
    const [context, setContext] = useState<ChatContext>({ messages: [] });
    const [threadId, setThreadId] = useState<string | null>(null);

    useEffect(() => {
        socket.on('thread_created', (data) => {
            setThreadId(data.thread_id);
            socket.emit('join_thread', { thread_id: data.thread_id });
        });

        socket.on('message_received', (data) => {
            setContext(prev => ({
                ...prev,
                messages: data.messages
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
            socket.off('thread_cleared');
        };
    }, []);

    const handleFileAnalysis = (content: string) => {
        // Request new thread when file is uploaded
        socket.emit('create_thread');
        setContext(prev => ({
            ...prev,
            csvContent: content
        }));
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

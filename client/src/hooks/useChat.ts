import { useState } from 'react';
import { Message, ChatContext } from '../types';

export function useChat() {
    const [context, setContext] = useState<ChatContext>({ messages: [] });

    const handleFileAnalysis = async (csvContent: string) => {
        setContext(prev => ({
            ...prev,
            csvContent,
            messages: [
                ...prev.messages,
                {
                    role: 'assistant',
                    content: 'I\'ve analyzed your CSV file. What would you like to know about it?',
                    timestamp: new Date()
                }
            ]
        }));
    };

    const handleSendMessage = async (content: string) => {
        const userMessage: Message = {
            role: 'user',
            content,
            timestamp: new Date()
        };

        setContext(prev => ({
            ...prev,
            messages: [...prev.messages, userMessage]
        }));

        // Placeholder for API call
        setTimeout(() => {
            const assistantMessage: Message = {
                role: 'assistant',
                content: `This is a placeholder response for: "${content}"`,
                timestamp: new Date()
            };
            setContext(prev => ({
                ...prev,
                messages: [...prev.messages, assistantMessage]
            }));
        }, 1000);
    };

    return {
        context,
        handleFileAnalysis,
        handleSendMessage
    };
}

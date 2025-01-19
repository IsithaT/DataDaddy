import { useState } from 'react';
import { Message, ChatContext } from '../types';

export function useChat() {
    const [context, setContext] = useState<ChatContext>({ messages: [] });

    const getPlaceholderResponse = (userMessage: string): Message => {
        const message = userMessage.toLowerCase();
        const response: Message = {
            role: 'assistant',
            content: '',
            timestamp: new Date()
        };
        if (message) {
            response.content = "Sample response text goes here. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac purus sit amet nunc fermentum aliquam. Donec auctor, nunc nec ultricies ultricies, nunc nunc fermentum nunc, nec fermentum nunc nunc nec nunc.";
            response.attachments = [{
                type: 'image',
                url: 'https://placehold.co/800x400/217f55/ffffff?text=Sample+Image',
                caption: 'Sample caption'
            }];
        }

        return response;
    };

    const handleFileAnalysis = async (csvContent: string) => {
        setContext(prev => ({
            ...prev,
            csvContent,
            messages: [
                ...prev.messages,
                {
                    role: 'assistant',
                    content: "I've loaded your CSV file and analyzed its structure. The data appears to contain multiple columns with numerical and categorical values. What would you like to know about your data?",
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

        // Simulate API delay
        setTimeout(() => {
            const assistantMessage = getPlaceholderResponse(content);
            setContext(prev => ({
                ...prev,
                messages: [...prev.messages, assistantMessage]
            }));
        }, 1000);
    };

    const clearContext = () => {
        setContext(prev => {
            const newContext: ChatContext = {
                csvContent: prev.csvContent,
                messages: prev.csvContent ? [{
                    role: 'assistant',
                    content: "I've loaded your CSV file and analyzed its structure. The data appears to contain multiple columns with numerical and categorical values. What would you like to know about your data?",
                    timestamp: new Date()
                }] : []
            };

            return newContext;
        });
    };

    return {
        context,
        handleFileAnalysis,
        handleSendMessage,
        clearContext
    };
}

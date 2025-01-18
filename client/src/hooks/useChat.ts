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

        if (message.includes('chart') || message.includes('graph') || message.includes('plot')) {
            response.content = "Based on your CSV data, I've generated a visualization that shows the key trends. Here's what we can observe from this chart:";
            response.attachments = [{
                type: 'chart',
                url: 'https://placehold.co/800x400/217f55/ffffff?text=Sample+Chart',
                caption: 'Visual representation of the analyzed data'
            }];
        } else if (message.includes('average') || message.includes('mean')) {
            response.content = "I've calculated the averages from your dataset. The mean value across the selected columns is approximately 42.5, with a standard deviation of 3.2.";
        } else if (message.includes('trend') || message.includes('pattern')) {
            response.content = "Looking at your data, I can identify several interesting patterns:\n\n1. There's a strong upward trend in the main metrics\n2. Seasonal variations occur every 3-4 months\n3. Peak values typically occur during Q4";
        } else if (message.includes('summary') || message.includes('overview')) {
            response.content = "Here's a quick summary of your dataset:\n\n• Total rows: 1,247\n• Columns: 8\n• Date range: Jan 2023 - Dec 2023\n• Key metrics show positive growth\n• No missing values detected";
            response.attachments = [{
                type: 'chart',
                url: 'https://placehold.co/800x400/217f55/ffffff?text=Sample+Chart',
                caption: 'Visual representation of the analyzed data'
            }];
        } else {
            response.content = "Based on the CSV data, I can help you analyze various aspects like trends, patterns, statistics, and generate visualizations. What specific insights would you like to explore?";
            response.attachments = [{
                type: 'image',
                url: 'https://placehold.co/800x400/217f55/ffffff?text=DATA+DADDY',
                caption: 'DATA DADDY REIGNS SUPREME'    
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

    return {
        context,
        handleFileAnalysis,
        handleSendMessage
    };
}

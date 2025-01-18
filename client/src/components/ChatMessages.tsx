import { useState, useRef, useEffect } from 'react';
import { Message } from '../types';
import { config } from '../config';

interface ChatMessagesProps {
    messages: Message[];
    onSendMessage: (content: string) => void;
}

export default function ChatMessages({ messages, onSendMessage }: ChatMessagesProps) {
    const [newMessage, setNewMessage] = useState('');
    const [isTyping, setIsTyping] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        // Add a small delay to account for image loading
        setTimeout(() => {
            messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
        }, 100);
    };

    useEffect(() => {
        if (messages.length > 0) {
            const lastMessage = messages[messages.length - 1];
            if (lastMessage.attachments?.length) {
                // For messages with images, wait a bit longer
                const img = new Image();
                img.onload = scrollToBottom;
                img.src = lastMessage.attachments[0].url;
            } else {
                scrollToBottom();
            }
        }
    }, [messages]);

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (newMessage.trim()) {
            setIsTyping(true);
            onSendMessage(newMessage);
            setNewMessage('');
            // Reset typing indicator after response
            setTimeout(() => setIsTyping(false), 1000);
        }
    };

    return (
        <div className="w-full mx-auto">
            <div className="bg-white rounded-lg shadow-sm border border-excel-300 h-[600px] overflow-y-auto py-4 px-12 mb-4 scroll-smooth">
                <div className="max-w-3xl mx-auto">
                    {messages.map((message, index) => (
                        <div
                            key={index}
                            className={`mb-6`}
                        >
                            <div className={`text-xl text-excel-600 mb-1 ${message.role === 'assistant' ? 'font-bold' : ''
                                }`}>
                                {message.role === 'assistant' ? config.assistant.name : 'You'}:
                            </div>
                            <div className="text-gray-800 whitespace-pre-wrap mb-2">
                                {message.content}
                            </div>
                            {message.attachments?.map((attachment, i) => (
                                <div key={i} className="mt-2">
                                    <img
                                        src={attachment.url}
                                        alt={attachment.caption || 'Analysis visualization'}
                                        className="rounded-lg border border-excel-300 w-full"
                                    />
                                    {attachment.caption && (
                                        <p className="text-sm text-excel-600 mt-1 italic">
                                            {attachment.caption}
                                        </p>
                                    )}
                                </div>

                            ))}
                            <br/>
                            <hr />
                        </div>
                    ))}
                    {isTyping && (
                        <div className="pl-4 text-excel-600">
                            {config.assistant.name} {config.assistant.typingText}
                        </div>
                    )}
                    <div ref={messagesEndRef} />
                </div>
            </div>
            <form onSubmit={handleSubmit} className="flex gap-2 max-w-3xl mx-auto">
                <input
                    type="text"
                    value={newMessage}
                    onChange={(e) => setNewMessage(e.target.value)}
                    placeholder="Ask a question about your data..."
                    className="flex-1 p-3 border border-excel-300 rounded-lg focus:outline-none focus:border-excel-600 text-lg"
                />
                <button type="submit" className="px-6 py-3 text-lg">
                    Send
                </button>
            </form>
        </div >
    );
}

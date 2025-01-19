import { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import { Message, MessageAttachment } from '../types';
import { config } from '../config';
import ImageCarousel from './ImageCarousel';

interface ChatMessagesProps {
    messages: Message[];
    onSendMessage: (content: string) => void;
    onClear: () => void;
    isTyping: boolean;
    images: MessageAttachment[];
    isImageCarouselOpen: boolean;
    setIsImageCarouselOpen: (isOpen: boolean) => void;
}

export default function ChatMessages({ 
    messages, 
    onSendMessage, 
    onClear, 
    isTyping,
    images,
    isImageCarouselOpen,
    setIsImageCarouselOpen 
}: ChatMessagesProps) {
    const [newMessage, setNewMessage] = useState('');
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
            onSendMessage(newMessage);
            setNewMessage('');
        }
    };

    return (
        <div className="h-full flex flex-col">
            <div className="bg-white rounded-lg shadow-sm border border-excel-300 overflow-y-auto p-12 mb-4 scroll-smooth max-h-[calc(90vh-12rem)]">
                <div className="max-w-3xl mx-auto">
                    {messages.map((message, index) => (
                        <div
                            key={index}
                            className={`mb-6 ${message.role === 'user' ? 'ml-auto' : 'mr-auto'} max-w-[80%] w-full ${
                                message.role === 'assistant' ? 'bg-excel-50/50 p-4 rounded-lg border border-excel-100' : ''
                            }`}
                        >
                            <div className={`text-xl text-excel-600 mb-1 ${
                                message.role === 'user' ? 'text-right' : 'text-left'
                            }`}>
                                {message.role === 'assistant' ? config.assistant.name : 'You'}:
                            </div>
                            {message.content && (
                                <div className={`text-gray-800 prose max-w-none ${
                                    message.role === 'user' ? 'text-right' : 'text-left'
                                }`}>
                                    <ReactMarkdown>
                                        {message.content}
                                    </ReactMarkdown>
                                </div>
                            )}
                        </div>
                    ))}
                    {isTyping && (
                        <div className="mr-auto max-w-[80%] w-full bg-excel-50/50 p-4 rounded-lg border border-excel-100">
                            <div className="text-xl text-excel-600 mb-1">
                                {config.assistant.name} {config.assistant.typingText}
                            </div>
                        </div>
                    )}
                    <div ref={messagesEndRef} />
                </div>
            </div>

            <ImageCarousel
                images={images}
                isOpen={isImageCarouselOpen}
                onClose={() => setIsImageCarouselOpen(false)}
            />

            <form onSubmit={handleSubmit} className="flex gap-2 w-full mx-auto">
                <input
                    type="text"
                    value={newMessage}
                    onChange={(e) => setNewMessage(e.target.value)}
                    placeholder="Ask a question about your data..."
                    className="flex-1 p-3 border border-excel-500 rounded-lg focus:outline-none 
                    hover:bg-excel-400 focus:border-excel-600 text-lg"
                />
                <button type="submit" className="px-6 py-3 text-lg">
                    Send
                </button>
                <button
                    onClick={onClear}
                    type="button"
                    className='px-6 py-3 text-lg bg-red-200 text-red-700 border border-red-300 rounded-lg hover:bg-red-400 hover:border-red-500 hover:text-red-950'
                >
                    Clear
                </button>
            </form>
        </div >
    );
}

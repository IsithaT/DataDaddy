import { useState } from 'react';
import { Message } from '../types';

interface ChatMessagesProps {
    messages: Message[];
    onSendMessage: (content: string) => void;
}

export default function ChatMessages({ messages, onSendMessage }: ChatMessagesProps) {
    const [newMessage, setNewMessage] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (newMessage.trim()) {
            onSendMessage(newMessage);
            setNewMessage('');
        }
    };

    return (
        <div className="w-full max-w-2xl mx-auto mt-4">
            <div className="bg-white rounded-lg shadow-sm border border-excel-300 h-[400px] overflow-y-auto p-4 mb-4">
                {messages.map((message, index) => (
                    <div 
                        key={index} 
                        className={`mb-4 ${
                            message.role === 'assistant' ? 'pl-4' : 'pl-2'
                        }`}
                    >
                        <div className={`text-sm text-excel-600 mb-1 ${
                            message.role === 'assistant' ? 'font-bold' : ''
                        }`}>
                            {message.role === 'assistant' ? 'Data Daddy' : 'You'}:
                        </div>
                        <div className="text-gray-800 whitespace-pre-wrap">
                            {message.content}
                        </div>
                    </div>
                ))}
            </div>
            <form onSubmit={handleSubmit} className="flex gap-2">
                <input
                    type="text"
                    value={newMessage}
                    onChange={(e) => setNewMessage(e.target.value)}
                    placeholder="Ask a question about your data..."
                    className="flex-1 p-2 border border-excel-300 rounded-lg focus:outline-none focus:border-excel-600"
                />
                <button type="submit" className="px-4 py-2">
                    Send
                </button>
            </form>
        </div>
    );
}

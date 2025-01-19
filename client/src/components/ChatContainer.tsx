import FileInput from './FileInput';
import ChatMessages from './ChatMessages';
import { useChat } from '../hooks/useChat';
import { config } from '../config';

export default function ChatContainer() {
    const { context, handleFileAnalysis, handleSendMessage, clearContext, isTyping } = useChat();

    return (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 h-full">
            <div className="lg:col-span-4 h-full overflow-auto">
                <div className="sticky top-0 p-2">
                    <FileInput onAnalysis={handleFileAnalysis} />
                </div>
            </div>
            <div className="lg:col-span-8 h-full">
                {context.csvContent ? (
                    <ChatMessages 
                        messages={context.messages} 
                        onSendMessage={handleSendMessage}
                        onClear={clearContext}
                        isTyping={isTyping}
                    />
                ) : (
                    <div className="h-full flex items-center justify-center text-excel-600 text-lg border-2 border-dashed border-excel-300 rounded-lg bg-white/50">
                        <div className="text-center px-4">
                            <h2 className="text-2xl font-bold mb-2">Welcome to {config.assistant.name}</h2>
                            <p>Upload a CSV file to start analyzing your data</p>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

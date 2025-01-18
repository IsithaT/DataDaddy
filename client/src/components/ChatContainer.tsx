import FileInput from './FileInput';
import ChatMessages from './ChatMessages';
import { useChat } from '../hooks/useChat';

export default function ChatContainer() {
    const { context, handleFileAnalysis, handleSendMessage } = useChat();

    return (
        <div className="w-full">
            <FileInput onAnalysis={handleFileAnalysis} />
            {context.csvContent && (
                <ChatMessages 
                    messages={context.messages} 
                    onSendMessage={handleSendMessage}
                />
            )}
        </div>
    );
}

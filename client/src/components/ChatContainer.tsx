import FileInput from './FileInput';
import ChatMessages from './ChatMessages';
import { useChat } from '../hooks/useChat';
import { config } from '../config';

export default function ChatContainer() {
    const { 
        context, 
        handleFileAnalysis, 
        handleSendMessage, 
        clearContext, 
        isTyping,
        images,
        isImageCarouselOpen,
        setIsImageCarouselOpen
    } = useChat();

    return (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 h-full">
            <div className="lg:col-span-4 h-full overflow-auto">
                <div className="sticky top-0 p-2 space-y-4">
                    <FileInput onAnalysis={handleFileAnalysis} />
                    {images.length > 0 && (
                        <button
                            onClick={() => setIsImageCarouselOpen(true)}
                            className="w-full bg-excel-100 hover:bg-excel-200 px-4 py-2 rounded-lg shadow-md"
                        >
                            View Visualizations ({images.length})
                        </button>
                    )}
                </div>
            </div>
            <div className="lg:col-span-8 h-full">
                {context.csvContent ? (
                    <ChatMessages 
                        messages={context.messages} 
                        onSendMessage={handleSendMessage}
                        onClear={clearContext}
                        isTyping={isTyping}
                        images={images}
                        isImageCarouselOpen={isImageCarouselOpen}
                        setIsImageCarouselOpen={setIsImageCarouselOpen}
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

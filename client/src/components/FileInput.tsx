import { useState } from 'react';

interface FileInputProps {
    onAnalysis: (content: string) => void;
}

export default function FileInput({ onAnalysis }: FileInputProps) {
    const [error, setError] = useState<string>('');
    const [csvContent, setCsvContent] = useState<string>('');
    const [isDragging, setIsDragging] = useState(false);

    const handleFileInput = (file: File | null) => {
        setError('');
        setCsvContent('');

        if (!file) return;

        if (!file.name.endsWith('.csv')) {
            setError('Please upload a CSV file');
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            const text = e.target?.result as string;
            setCsvContent(text);
            onAnalysis(text);
        };
        reader.readAsText(file);
    };

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0];
        if (file) {
            handleFileInput(file);
            if (!file?.name.endsWith('.csv')) {
                event.target.value = '';
            }
        }
    };

    const handleDragOver = (e: React.DragEvent<HTMLLabelElement>) => {
        e.preventDefault();
        setIsDragging(true);
    };

    const handleDragLeave = (e: React.DragEvent<HTMLLabelElement>) => {
        e.preventDefault();
        setIsDragging(false);
    };

    const handleDrop = (e: React.DragEvent<HTMLLabelElement>) => {
        e.preventDefault();
        setIsDragging(false);
        const file = e.dataTransfer.files[0];
        handleFileInput(file);
    };

    return (
        <div className="flex flex-col gap-4 w-full">
            <div className="w-full">
                <label
                    htmlFor="fileInput"
                    className={`flex flex-col items-center w-full p-6 border-2 border-dashed rounded-lg cursor-pointer bg-white transition-colors ${isDragging ? 'border-excel-600 bg-excel-50' : 'border-excel-300 hover:bg-excel-50'
                        }`}
                    onDragOver={handleDragOver}
                    onDragLeave={handleDragLeave}
                    onDrop={handleDrop}
                >
                    <svg className="w-8 h-8 text-excel-600 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                    </svg>
                    <span className="text-excel-600">Choose a CSV file or drag it here</span>
                </label>
                <input
                    id="fileInput"
                    type="file"
                    accept=".csv"
                    onChange={handleFileChange}
                    className="hidden"
                />
            </div>
            {error && (
                <div className="text-red-500 text-sm">{error}</div>
            )}
            {csvContent && (
                <div className="w-full mt-4 ">
                    <h2 className="text-xl mb-2 text-excel-600">CSV Content:</h2>
                    <pre className="bg-white p-4 max-h-64 text-left overflow-auto rounded-lg border border-excel-300 overflow-x-auto text-[0.5rem]">
                        {csvContent}
                    </pre>
                </div>
            )}
        </div>
    );
}
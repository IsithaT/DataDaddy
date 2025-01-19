import { useState } from 'react';
import { MessageAttachment } from '../types';

interface ImageCarouselProps {
    images: MessageAttachment[];
    isOpen: boolean;
    onClose: () => void;
}

export default function ImageCarousel({ images, isOpen, onClose }: ImageCarouselProps) {
    const [currentIndex, setCurrentIndex] = useState(0);

    if (!isOpen || images.length === 0) return null;

    const handleNext = () => {
        setCurrentIndex((prev) => (prev + 1) % images.length);
    };

    const handlePrev = () => {
        setCurrentIndex((prev) => (prev - 1 + images.length) % images.length);
    };

    const handleOverlayClick = (e: React.MouseEvent) => {
        if (e.target === e.currentTarget) {
            onClose();
        }
    };

    return (
        <div 
            className="fixed inset-0 backdrop-blur-sm bg-black/40 flex items-center justify-center z-50 transition-opacity duration-300"
            onClick={handleOverlayClick}
        >
            <div className="bg-white/95 rounded-2xl p-12 max-w-3xl w-full mx-4 relative shadow-2xl transform transition-transform duration-300">
                <button
                    onClick={onClose}
                    className="absolute top-2 right-2 bg-transparent flex space-x-2 items-center p-1 text-gray-600 hover:text-gray-800 hover:bg-excel-100 rounded-lg transition-colors"
                    aria-label="Close"
                >

                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>

                <div className="relative">
                    <div className="aspect-[16/9] bg-black/5 rounded-lg overflow-hidden">
                        <img
                            src={images[currentIndex].url}
                            alt={images[currentIndex].caption || 'Visualization'}
                            className="w-full h-full object-contain transition-opacity duration-300"
                        />
                    </div>

                </div>

                {images.length > 1 && (
                    <div className="flex justify-between items-center mt-6">
                        <button
                            onClick={handlePrev}
                            className="px-6 py-3 bg-excel-600 text-white rounded-lg hover:bg-excel-700 transition-colors shadow-md hover:shadow-lg flex items-center gap-2"
                        >
                            ← Previous
                        </button>
                        <span className="text-excel-600 font-medium bg-excel-50 px-4 py-2 rounded-full">
                            {currentIndex + 1} of {images.length}
                        </span>
                        <button
                            onClick={handleNext}
                            className="px-6 py-3 bg-excel-600 text-white rounded-lg hover:bg-excel-700 transition-colors shadow-md hover:shadow-lg flex items-center gap-2"
                        >
                            Next →
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
}

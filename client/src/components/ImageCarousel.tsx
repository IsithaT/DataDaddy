import { useState } from 'react';
import { Attachment } from '../types';

interface ImageCarouselProps {
    images: Attachment[];
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

    return (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
            <div className="bg-white rounded-lg p-4 max-w-4xl w-full mx-4 relative">
                <button 
                    onClick={onClose}
                    className="absolute -top-2 -right-2 bg-red-500 text-white w-8 h-8 rounded-full flex items-center justify-center hover:bg-red-600 z-10"
                >
                    ×
                </button>
                
                <div className="relative aspect-video">
                    <img
                        src={images[currentIndex].url}
                        alt={images[currentIndex].caption || 'Visualization'}
                        className="w-full h-full object-contain"
                    />
                    {images[currentIndex].caption && (
                        <p className="text-sm text-excel-600 mt-2 italic text-center">
                            {images[currentIndex].caption}
                        </p>
                    )}
                </div>

                {images.length > 1 && (
                    <div className="flex justify-between mt-4">
                        <button 
                            onClick={handlePrev}
                            className="px-4 py-2 bg-excel-100 hover:bg-excel-200 rounded"
                        >
                            Previous
                        </button>
                        <span className="text-excel-600">
                            {currentIndex + 1} / {images.length}
                        </span>
                        <button 
                            onClick={handleNext}
                            className="px-4 py-2 bg-excel-100 hover:bg-excel-200 rounded"
                        >
                            Next
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
}

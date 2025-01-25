import { useState, useEffect } from 'react';
import ChatContainer from './components/ChatContainer';
import { config } from './config';
import './App.css';
import { socket } from './utils/socket';

export default function App() {
  const [apiKey, setApiKey] = useState(localStorage.getItem('openai_api_key') || '');
  const [isValidating, setIsValidating] = useState(false);
  const [isValidKey, setIsValidKey] = useState(false);
  const [error, setError] = useState('');

  const validateApiKey = async (key: string) => {
    setIsValidating(true);
    setError('');
    
    try {
      const response = await fetch('https://api.openai.com/v1/models', {
        headers: {
          'Authorization': `Bearer ${key}`
        }
      });

      const isValid = response.status === 200;
      setIsValidKey(isValid);
      
      if (isValid) {
        socket.emit('set_api_key', key);
        localStorage.setItem('openai_api_key', key);
        setError('');
      } else {
        setError('Invalid API key. Please check and try again.');
      }
    } catch {
      setIsValidKey(false);
      setError('Error validating API key. Please try again.');
    } finally {
      setIsValidating(false);
    }
  };

  useEffect(() => {
    socket.connect();

    socket.on('connect', () => {
      console.log('Socket connected');
      if (apiKey) {
        validateApiKey(apiKey);
      }
    });

    socket.on('connection_status', (status: { connected: boolean }) => {
      console.log('Connection status:', status.connected);
    });

    return () => {
      socket.off('connect');
      socket.off('connection_status');
    };
  }, [apiKey]);

  const handleApiKeySubmit = (e: React.FormEvent) => {
    e.preventDefault();
    validateApiKey(apiKey);
  };

  const handleChangeApiKey = () => {
    setIsValidKey(false);
    setApiKey('');
    localStorage.removeItem('openai_api_key');
  };

  return (
    <div className="bg-[#f5f7f5]">
      
      {!isValidKey ? (
        
        <div className="flex items-center justify-center flex-col gap-12 p-4 min-h-[75vh]">
          <h1 className="md:text-[3em] text-[1.8rem] leading-[1.1] text-excel-900">
            {config.assistant.name + ": CSV Analyzing Assistant"}
          </h1>
          <div className='flex items-center justify-center flex-col gap-4'>
            <div className="bg-excel-50 p-8 mb-4 rounded-lg shadow-md w-full max-w-md border border-excel-300">
              <h2 className="md:text-xl text-lg font-bold mb-6 text-center text-excel-600">
                Enter your OpenAI API Key to get started
              </h2>
              <form onSubmit={handleApiKeySubmit}>
                <div className="mb-4">
                  <input
                    type="password"
                    placeholder="sk-..."
                    value={apiKey}
                    onChange={(e) => setApiKey(e.target.value)}
                    className={`w-full p-3 border rounded-md focus:outline-none focus:ring-2
                      ${error ? 'border-red-500 focus:ring-red-200' : 'border-excel-300 focus:ring-[#7ed3aa]'}`}
                    disabled={isValidating}
                  />
                  {error && <p className="mt-2 text-sm text-red-600">{error}</p>}
                </div>
                <button
                  type="submit"
                  disabled={isValidating || !apiKey}
                  className={`w-full p-3 rounded-md text-white font-medium
                    ${isValidating || !apiKey
                      ? 'bg-gray-400 cursor-not-allowed'
                      : 'bg-[#2b9d6a] hover:bg-[#217f55] border border-[#4ab785] hover:border-[#217f55]'}`}
                >
                  {isValidating ? 'Validating...' : 'Submit API Key'}
                </button>
                <p className="mt-4 text-sm text-[#184432] text-center">
                  Your API key is stored locally and securely transmitted to our server through an encrypted WebSocket connection.
                </p>
              </form>
            </div>
            <p className="text-sm">
              Your OpenAI API key is required to process your requests. The key is stored locally 
              and transmitted securely to handle your analysis requests.
              You can get your API key from the <a href="https://platform.openai.com/api-keys" target="_blank" rel="noopener noreferrer" className="text-[#2b9d6a] hover:text-[#217f55] underline">OpenAI platform</a>.
            </p>
            <p className="text-sm text-gray-600">
              View this project on <a href="https://github.com/IsithaT/DataDave" target="_blank" rel="noopener noreferrer" className="text-[#2b9d6a] hover:text-[#217f55] underline">GitHub</a>
            </p>
          </div>
        </div>
      ) : (
        <div className="container mx-auto px-4 py-8">
          <div className="flex justify-between items-center mb-8 md:flex-row flex-col gap-4">
              <h1 className="md:text-[3em] text-[1.8rem] leading-[1.1] text-excel-900">
              {config.assistant.name + ": CSV Analyzing Assistant"}
            </h1>
            <button
              onClick={handleChangeApiKey}
              className="md:px-4 md:py-2 md:text-base text-xs px-2 py-1 rounded-md border border-[#4ab785] bg-[#2b9d6a] hover:bg-[#217f55] hover:border-[#217f55] text-white font-medium transition-colors duration-200"
            >
              Change API Key
            </button>
          </div>
          <ChatContainer />
        </div>
      )}
    </div>
  );
}

import io from 'socket.io-client';

const SOCKET_URL = import.meta.env.PROD
    ? `${import.meta.env.VITE_SERVER_URL}`
    : 'http://localhost:5000';

// Add connection state management
let isConnected = false;

export const socket = io(SOCKET_URL, {
    autoConnect: true,
    transports: ['polling', 'websocket'],
    reconnection: true,
    reconnectionAttempts: 5,
    reconnectionDelay: 1000,
    secure: true,
    path: '/socket.io/'
});

socket.on('connect', () => {
    console.log('Socket connected:', socket.id);
    isConnected = true;
});

socket.on('disconnect', () => {
    console.log('Socket disconnected');
    isConnected = false;
});

socket.on('connect_error', (error: Error) => {
    console.error('Connection error:', error);
    isConnected = false;
    if (import.meta.env.DEV) {
        console.log('Connection URL:', SOCKET_URL);
    }
});

// Add helper to check connection status
export const isSocketConnected = () => isConnected;

// Explicitly connect socket
socket.connect();
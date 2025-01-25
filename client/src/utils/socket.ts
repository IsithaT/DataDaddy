import io from 'socket.io-client';

const SOCKET_URL = import.meta.env.PROD
    ? `${import.meta.env.VITE_SERVER_URL}`
    : 'http://localhost:5000';

export const socket = io(SOCKET_URL, {
    autoConnect: true,
    transports: ['websocket', 'polling'],
    reconnection: true,
    reconnectionAttempts: 5,
    reconnectionDelay: 1000,
    secure: import.meta.env.PROD,
    path: '/socket.io/'
});

socket.on('connect', () => {
    console.log('Socket connected:', socket.id);
});

socket.on('connect_error', (error: Error) => {
    console.error('Connection error:', error);
    if (import.meta.env.DEV) {
        console.log('Connection URL:', SOCKET_URL);
    }
});
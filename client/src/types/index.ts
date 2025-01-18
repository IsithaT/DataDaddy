export type Role = 'user' | 'assistant' | 'system';

export interface Message {
    role: Role;
    content: string;
    timestamp: Date;
}

export interface ChatContext {
    messages: Message[];
    csvContent?: string;
}

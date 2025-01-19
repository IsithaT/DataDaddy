export type Role = 'user' | 'assistant' | 'system';

export interface MessageAttachment {
    type: 'image' | 'chart';
    url: string;
    caption?: string;
}

export interface Message {
    role: Role;
    content: string;
    timestamp: Date;
    attachments?: MessageAttachment[];
}

export interface ChatContext {
    messages: Message[];
    csvContent?: string;
}

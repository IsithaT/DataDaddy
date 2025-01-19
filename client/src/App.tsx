import ChatContainer from './components/ChatContainer';
import { config } from './config';
import './App.css';

function App() {
  return (
    <div className="">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-center mb-8">{config.assistant.name}</h1>
        <ChatContainer />
      </div>
    </div>
  );
}

export default App;

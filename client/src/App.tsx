import ChatContainer from './components/ChatContainer';
import { config } from './config';
import './App.css';

function App() {
  return (
    <div className="">
      <div className="container mx-auto">
        <h1 className="text-center mb-8">{config.assistant.name + ": CSV Analyzing Assistant"} </h1>
        <ChatContainer />
      </div>
    </div>
  );
}

export default App;

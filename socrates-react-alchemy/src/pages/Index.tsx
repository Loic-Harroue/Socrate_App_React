
import { useState } from 'react';
import Sidebar from '@/components/Sidebar';
import ChatPage from '@/components/pages/ChatPage';
import KeywordsPage from '@/components/pages/KeywordsPage';
import SynonymesPage from '@/components/pages/SynonymesPage';
import ClusterPage from '@/components/pages/ClusterPage';
import ClusterZeroPage from '@/components/pages/ClusterZeroPage';
import PromptsPage from '@/components/pages/PromptsPage';
import LogsPage from '@/components/pages/LogsPage';

const Index = () => {
  const [activePage, setActivePage] = useState('ai_chat');
  const [selectedModel, setSelectedModel] = useState('');
  const [selectedSubmodel, setSelectedSubmodel] = useState('');
  const [selectedScience, setSelectedScience] = useState('datasocial');

  const renderActivePage = () => {
    switch (activePage) {
      case 'ai_chat':
        return <ChatPage 
          selectedModel={selectedModel}
          selectedSubmodel={selectedSubmodel}
          selectedScience={selectedScience}
        />;
      case 'process_keywords':
        return <KeywordsPage 
          selectedModel={selectedModel}
          selectedSubmodel={selectedSubmodel}
          selectedScience={selectedScience}
        />;
      case 'process_synonyms':
        return <SynonymesPage 
          selectedModel={selectedModel}
          selectedSubmodel={selectedSubmodel}
          selectedScience={selectedScience}
        />;
      case 'process_clusters':
        return <ClusterPage 
          selectedModel={selectedModel}
          selectedSubmodel={selectedSubmodel}
          selectedScience={selectedScience}
        />;
      case 'process_clusters_zero':
        return <ClusterZeroPage 
          selectedModel={selectedModel}
          selectedSubmodel={selectedSubmodel}
          selectedScience={selectedScience}
        />;
      case 'prompts':
        return <PromptsPage />;
      case 'logs':
        return <LogsPage />;
      default:
        return <ChatPage 
          selectedModel={selectedModel}
          selectedSubmodel={selectedSubmodel}
          selectedScience={selectedScience}
        />;
    }
  };

  return (
    <div className="flex min-h-screen bg-background">
      <Sidebar 
        activePage={activePage}
        setActivePage={setActivePage}
        selectedModel={selectedModel}
        setSelectedModel={setSelectedModel}
        selectedSubmodel={selectedSubmodel}
        setSelectedSubmodel={setSelectedSubmodel}
        selectedScience={selectedScience}
        setSelectedScience={setSelectedScience}
      />
      <main className="flex-1 p-6">
        {renderActivePage()}
      </main>
    </div>
  );
};

export default Index;

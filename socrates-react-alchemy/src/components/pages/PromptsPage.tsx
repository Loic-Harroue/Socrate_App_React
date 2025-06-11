
import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Textarea } from '@/components/ui/textarea';
import { Button } from '@/components/ui/button';
import { FileEdit } from 'lucide-react';

const PromptsPage = () => {
  const [promptText, setPromptText] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedLevel, setSelectedLevel] = useState('');

  const getCookie = (name: string) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let c of cookies) {
        const cookie = c.trim();
        if (cookie.startsWith(name + '=')) {
          cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

  const handleLoadPrompt = async () => {
    if (!selectedCategory || !selectedLevel) {
      alert("Veuillez sélectionner une catégorie et un niveau.");
      return;
    }

    const url = `/ajax/get-prompt/?category_ref=${selectedCategory}&level_ref=${selectedLevel}`;
    
    try {
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'X-CSRFToken': getCookie('csrftoken')
        }
      });

      if (!response.ok) throw new Error("Erreur lors du chargement du prompt.");
      
      const data = await response.json();
      setPromptText(data.prompt_text || 'Aucun prompt trouvé.');
    } catch (error) {
      console.error("Erreur récupération du prompt :", error);
      alert("Impossible de récupérer le prompt.");
    }
  };

  // Note: In a real implementation, you would get these from your sidebar state
  // For now, I'm adding the button to trigger the load manually
  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <FileEdit className="h-6 w-6 text-blue-600" />
            Gestion des prompts
          </CardTitle>
        </CardHeader>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Contenu du prompt</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <Button 
            onClick={handleLoadPrompt}
            className="bg-blue-600 hover:bg-blue-700"
          >
            Charger le prompt
          </Button>
          <Textarea
            value={promptText}
            onChange={(e) => setPromptText(e.target.value)}
            placeholder="Le contenu du prompt apparaîtra ici après sélection d'une catégorie et d'un niveau..."
            className="min-h-64"
            readOnly
          />
        </CardContent>
      </Card>
    </div>
  );
};

export default PromptsPage;

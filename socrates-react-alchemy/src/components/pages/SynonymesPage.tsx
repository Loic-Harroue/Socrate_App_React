
import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { BookOpen, Loader2 } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

interface SynonymesPageProps {
  selectedModel: string;
  selectedSubmodel: string;
  selectedScience: string;
}

const SynonymesPage = ({ selectedModel, selectedSubmodel, selectedScience }: SynonymesPageProps) => {
  const [word, setWord] = useState('');
  const [synonyms, setSynonyms] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [responseTime, setResponseTime] = useState<number | null>(null);
  const { toast } = useToast();

  const getCookie = (name: string) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

  const handleFindSynonyms = async () => {
    if (!word.trim()) {
      toast({
        title: "Erreur",
        description: "Veuillez saisir un mot pour l'analyse",
        variant: "destructive"
      });
      return;
    }

    if (!selectedModel || !selectedSubmodel) {
      toast({
        title: "Erreur",
        description: "Veuillez sélectionner un modèle et un sous-modèle",
        variant: "destructive"
      });
      return;
    }

    setIsLoading(true);
    const startTime = performance.now();

    const payload = {
      model: selectedModel,
      sous_model: selectedSubmodel,
      user_artirev: "API",
      words: word,
      dataset_type: selectedScience
    };

    try {
      const response = await fetch('/ajax/synonymes/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(payload)
      });

      const data = await response.json();
      const endTime = performance.now();

      if (data.error) {
        throw new Error(data.error);
      } else if (data.synonyms) {
        setSynonyms(data.synonyms);
        setResponseTime((endTime - startTime) / 1000);
        
        toast({
          title: "Succès",
          description: "Synonymes trouvés avec succès",
        });
      } else {
        setSynonyms([]);
        toast({
          title: "Information",
          description: "Aucun synonyme trouvé",
        });
      }
    } catch (error) {
      console.error("Erreur API :", error);
      toast({
        title: "Erreur",
        description: "Une erreur est survenue lors de la recherche",
        variant: "destructive"
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleFindSynonyms();
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <BookOpen className="h-6 w-6 text-blue-600" />
            Recherche de synonymes
          </CardTitle>
        </CardHeader>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Mot à analyser</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <Input
            value={word}
            onChange={(e) => setWord(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Saisissez le mot à analyser..."
            className="text-lg"
          />
          <Button
            onClick={handleFindSynonyms}
            disabled={isLoading || !word.trim()}
            className="bg-blue-600 hover:bg-blue-700"
          >
            {isLoading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Recherche en cours...
              </>
            ) : (
              'Trouver les synonymes'
            )}
          </Button>
        </CardContent>
      </Card>

      {synonyms.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Synonymes trouvés</CardTitle>
            {responseTime && (
              <p className="text-sm text-muted-foreground">
                Temps de réponse: {responseTime.toFixed(2)} secondes
              </p>
            )}
          </CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-2">
              {synonyms.map((synonym, index) => (
                <Badge key={index} variant="outline" className="text-sm">
                  {synonym}
                </Badge>
              ))}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default SynonymesPage;

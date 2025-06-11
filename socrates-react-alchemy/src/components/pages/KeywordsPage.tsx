
import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Key, Loader2 } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

interface KeywordsPageProps {
  selectedModel: string;
  selectedSubmodel: string;
  selectedScience: string;
}

const KeywordsPage = ({ selectedModel, selectedSubmodel, selectedScience }: KeywordsPageProps) => {
  const [sourceText, setSourceText] = useState('');
  const [keywords, setKeywords] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [responseTime, setResponseTime] = useState<number | null>(null);
  const { toast } = useToast();

  const handleExtractKeywords = async () => {
    if (!sourceText.trim()) {
      toast({
        title: "Erreur",
        description: "Veuillez saisir du texte pour l'analyse",
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
      question: sourceText,
      dataset_type: selectedScience
    };

    try {
      const response = await fetch('/ajax/keywords/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(payload)
      });

      const data = await response.json();
      
      if (data && data.keywords) {
        setKeywords(data.keywords);
        const endTime = performance.now();
        setResponseTime((endTime - startTime) / 1000);
        
        toast({
          title: "Succès",
          description: "Mots-clés extraits avec succès",
        });
      } else {
        throw new Error("Aucune donnée reçue");
      }
    } catch (error) {
      console.error("Erreur appel keywords :", error);
      toast({
        title: "Erreur",
        description: "Une erreur est survenue lors de l'extraction",
        variant: "destructive"
      });
    } finally {
      setIsLoading(false);
    }
  };

  // Helper function to get CSRF token
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

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Key className="h-6 w-6 text-blue-600" />
            Extraction de mots-clés
          </CardTitle>
        </CardHeader>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Texte source</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <Textarea
            value={sourceText}
            onChange={(e) => setSourceText(e.target.value)}
            placeholder="Saisissez le texte à analyser..."
            className="min-h-32"
          />
          <Button
            onClick={handleExtractKeywords}
            disabled={isLoading || !sourceText.trim()}
            className="bg-blue-600 hover:bg-blue-700"
          >
            {isLoading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Extraction en cours...
              </>
            ) : (
              'Extraire les mots-clés'
            )}
          </Button>
        </CardContent>
      </Card>

      {keywords.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Mots-clés extraits</CardTitle>
            {responseTime && (
              <p className="text-sm text-muted-foreground">
                Temps de réponse: {responseTime.toFixed(2)} secondes
              </p>
            )}
          </CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-2">
              {keywords.map((keyword, index) => (
                <Badge key={index} variant="secondary" className="text-sm">
                  {keyword}
                </Badge>
              ))}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default KeywordsPage;

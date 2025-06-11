
import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { GitBranch, Download, FileText } from 'lucide-react';

interface ClusterZeroPageProps {
  selectedModel: string;
  selectedSubmodel: string;
  selectedScience: string;
}

const ClusterZeroPage = ({ selectedModel, selectedSubmodel, selectedScience }: ClusterZeroPageProps) => {
  const [results, setResults] = useState<any>(null);
  const [responseTime, setResponseTime] = useState<number | null>(null);

  const handleGeneratePDF = () => {
    // Mock PDF generation
    console.log('Generating PDF...');
  };

  const handleGenerateDOCX = () => {
    // Mock DOCX generation
    console.log('Generating DOCX...');
  };

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <GitBranch className="h-6 w-6 text-blue-600" />
            Analyse de Clusters Zero
          </CardTitle>
        </CardHeader>
      </Card>

      {results && (
        <>
          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Résultats de l'analyse</CardTitle>
              {responseTime && (
                <p className="text-sm text-muted-foreground">
                  Temps de réponse: {responseTime.toFixed(2)} secondes
                </p>
              )}
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                <Button
                  onClick={handleGeneratePDF}
                  variant="outline"
                  className="flex items-center gap-2"
                >
                  <Download className="h-4 w-4" />
                  Générer PDF
                </Button>
                
                <Button
                  onClick={handleGenerateDOCX}
                  variant="outline"
                  className="flex items-center gap-2"
                >
                  <FileText className="h-4 w-4" />
                  Générer DOCX
                </Button>
              </div>

              <div className="bg-gray-50 p-4 rounded-lg">
                <p className="text-sm text-gray-600">
                  L'éditeur JSON avec les résultats apparaîtra ici après le traitement du fichier Excel.
                </p>
              </div>
            </CardContent>
          </Card>
        </>
      )}

      {!results && (
        <Card>
          <CardContent className="p-8 text-center">
            <GitBranch className="h-16 w-16 mx-auto mb-4 text-gray-400" />
            <h3 className="text-lg font-semibold mb-2">Analysez vos données</h3>
            <p className="text-muted-foreground">
              Uploadez un fichier Excel (.xlsx) via la sidebar pour commencer l'analyse de clusters zero.
            </p>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default ClusterZeroPage;

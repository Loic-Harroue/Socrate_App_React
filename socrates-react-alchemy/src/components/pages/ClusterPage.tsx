
import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { GitBranch, Download, FileText, Languages } from 'lucide-react';
import { getClustersColors } from '@/utils/colors';

interface ClusterPageProps {
  selectedModel: string;
  selectedSubmodel: string;
  selectedScience: string;
}

const ClusterPage = ({ selectedModel, selectedSubmodel, selectedScience }: ClusterPageProps) => {
  const [results, setResults] = useState<any>(null);
  const [responseTime, setResponseTime] = useState<number | null>(null);
  const [rawJsonResponse, setRawJsonResponse] = useState<any>(null);

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

  const renderClusterResults = (data: any, responseTime: number) => {
    const colors = getClustersColors(data.clusters?.length || 0);
    
    return (
      <div className="space-y-6">
        <div className="bg-white p-6 rounded-lg shadow-sm border">
          <h2 className="text-xl font-semibold mb-4">{data.main_title || 'Résultats de l\'analyse des clusters'}</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
            <div><strong>Modèle :</strong> {data.result_model}</div>
            <div><strong>Coût :</strong> {data.couts}</div>
            <div><strong>Prompt tokens :</strong> {data.prompt_token}</div>
            <div><strong>Completion tokens :</strong> {data.completion_token}</div>
          </div>
          <div className="mt-2 text-sm">
            <strong>Temps de réponse API :</strong> {responseTime.toFixed(2)} s
          </div>
        </div>

        {data.clusters?.map((cluster: any, index: number) => {
          const color = colors[index % colors.length];
          return (
            <div key={index} className="bg-white p-6 rounded-lg shadow-sm border">
              <h3 className="text-lg font-semibold mb-2" style={{ color: color.hexa }}>
                Cluster {cluster.cluster} — {cluster.common_theme}
              </h3>
              <p className="mb-4">{cluster.summary}</p>

              {cluster.subthemes && cluster.subthemes.length > 0 && (
                <div className="mb-4">
                  <h4 className="font-medium mb-2">{data.sub_title2 || 'Subthemes'}</h4>
                  <ul className="list-disc list-inside space-y-1">
                    {cluster.subthemes.map((sub: any, subIndex: number) => (
                      <li key={subIndex}>
                        <strong>{sub.subtheme_type}</strong>: {sub.subtheme_citations.join(', ')}
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {cluster.outliers && cluster.outliers.length > 0 && (
                <div>
                  <h5 className="font-medium mb-2">{data.sub_title3 || 'Citations hors sous-thèmes'}</h5>
                  <ul className="list-disc list-inside space-y-1">
                    {cluster.outliers.map((citation: string, outIndex: number) => (
                      <li key={outIndex}>{citation}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          );
        })}
      </div>
    );
  };

  const handleGeneratePDF = async () => {
    if (!rawJsonResponse) {
      alert("Aucune donnée à exporter.");
      return;
    }

    try {
      const response = await fetch("process_clusters/ajax/generate_pdf/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(rawJsonResponse),
      });

      if (!response.ok) {
        throw new Error('Erreur lors de la génération du PDF');
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = "summary.pdf";
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(url);
    } catch (error: any) {
      alert("Erreur PDF : " + error.message);
      console.error(error);
    }
  };

  const handleGenerateDOCX = async () => {
    if (!rawJsonResponse) {
      alert("Aucune donnée à exporter.");
      return;
    }

    try {
      const response = await fetch("process_clusters/ajax/generate_docx/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(rawJsonResponse),
      });

      if (!response.ok) {
        throw new Error('Erreur lors de la génération du DOCX');
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = "summary.docx";
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(url);
    } catch (error: any) {
      alert("Erreur DOCX : " + error.message);
      console.error(error);
    }
  };

  const handleTranslate = async () => {
    if (!rawJsonResponse) {
      alert("Aucun résultat JSON à traduire.");
      return;
    }

    const clustersToTranslate = rawJsonResponse.clusters;
    const payload = {
      model: selectedModel,
      sous_model: selectedSubmodel,
      user_artirev: "API",
      data: clustersToTranslate
    };

    try {
      const start = performance.now();
      const response = await fetch("/ajax/translate/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      const end = performance.now();

      if (response.ok) {
        setRawJsonResponse(data);
        setResults(renderClusterResults(data, (end - start) / 1000));
        setResponseTime((end - start) / 1000);
      } else {
        alert(data.error || "Erreur lors de la traduction.");
      }
    } catch (error) {
      console.error("Erreur lors de la requête de traduction :", error);
      alert("Une erreur s'est produite lors de la traduction.");
    }
  };

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <GitBranch className="h-6 w-6 text-blue-600" />
            Analyse de Clusters
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
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
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
                
                <Button
                  onClick={handleTranslate}
                  variant="outline"
                  className="flex items-center gap-2"
                >
                  <Languages className="h-4 w-4" />
                  Traduire et rafficher
                </Button>
              </div>

              {results}
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
              Uploadez un fichier Excel (.xlsx) via la sidebar pour commencer l'analyse de clusters.
            </p>
          </CardContent>
        </Card>
      )}
    </div>
  );
};

export default ClusterPage;

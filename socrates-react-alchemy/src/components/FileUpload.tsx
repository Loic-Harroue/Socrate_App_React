
import { useState, useRef } from 'react';
import { Upload } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

interface FileUploadProps {
  activePage: string;
  selectedModel: string;
  selectedSubmodel: string;
  selectedScience: string;
}

const FileUpload = ({ activePage, selectedModel, selectedSubmodel, selectedScience }: FileUploadProps) => {
  const [isDragging, setIsDragging] = useState(false);
  const [uploadStatus, setUploadStatus] = useState('');
  const [isUploading, setIsUploading] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const { toast } = useToast();

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      handleFileUpload(files[0]);
    }
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      handleFileUpload(files[0]);
    }
  };

  const handleFileUpload = async (file: File) => {
    if (!file.name.endsWith('.xlsx')) {
      toast({
        title: "Erreur",
        description: "Veuillez sélectionner un fichier .xlsx",
        variant: "destructive"
      });
      return;
    }

    if (!selectedModel || !selectedSubmodel || !selectedScience) {
      toast({
        title: "Erreur",
        description: "Veuillez sélectionner un modèle, sous-modèle et science",
        variant: "destructive"
      });
      return;
    }

    setIsUploading(true);
    setUploadStatus('Traitement en cours...');

    const formData = new FormData();
    formData.append('file', file);
    formData.append('model', selectedModel);
    formData.append('sous_model', selectedSubmodel);
    formData.append('dataset_type', selectedScience);

    try {
      // Simulate API call for now
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      setUploadStatus('Fichier traité avec succès');
      toast({
        title: "Succès",
        description: "Le fichier a été traité avec succès",
      });

      // Here you would dispatch the results to the appropriate page component
      console.log('File processed for page:', activePage);
      
    } catch (error) {
      setUploadStatus('Erreur lors du traitement');
      toast({
        title: "Erreur",
        description: "Une erreur est survenue lors du traitement",
        variant: "destructive"
      });
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="space-y-4">
      <div
        className={`
          border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors
          ${isDragging ? 'border-blue-500 bg-blue-50' : 'border-gray-300 hover:border-gray-400'}
          ${isUploading ? 'opacity-50 cursor-not-allowed' : ''}
        `}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => !isUploading && fileInputRef.current?.click()}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept=".xlsx"
          onChange={handleFileSelect}
          className="hidden"
          disabled={isUploading}
        />
        
        <Upload className="mx-auto h-12 w-12 text-gray-400 mb-4" />
        <p className="text-sm">
          <span className="font-semibold">Drag and drop file here</span>
          <br />
          <span className="text-gray-500">Limit 200MB per file • XLSX</span>
        </p>
      </div>

      {uploadStatus && (
        <div className={`text-sm p-3 rounded ${
          uploadStatus.includes('succès') ? 'bg-green-100 text-green-800' : 
          uploadStatus.includes('Erreur') ? 'bg-red-100 text-red-800' : 
          'bg-blue-100 text-blue-800'
        }`}>
          {uploadStatus}
        </div>
      )}
    </div>
  );
};

export default FileUpload;

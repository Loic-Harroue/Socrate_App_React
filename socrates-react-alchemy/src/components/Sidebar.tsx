
import { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Card, CardContent } from '@/components/ui/card';
import { Label } from '@/components/ui/label';
import FileUpload from '@/components/FileUpload';
import { useToast } from '@/hooks/use-toast';

interface SidebarProps {
  activePage: string;
  setActivePage: (page: string) => void;
  selectedModel: string;
  setSelectedModel: (model: string) => void;
  selectedSubmodel: string;
  setSelectedSubmodel: (submodel: string) => void;
  selectedScience: string;
  setSelectedScience: (science: string) => void;
}

interface Model {
  model_id: number;
  model_name: string;
}

interface Category {
  ref: string;
  name: string;
}

const Sidebar = ({
  activePage,
  setActivePage,
  selectedModel,
  setSelectedModel,
  selectedSubmodel,
  setSelectedSubmodel,
  selectedScience,
  setSelectedScience
}: SidebarProps) => {
  const [version, setVersion] = useState('');
  const [models, setModels] = useState<Model[]>([]);
  const [submodels, setSubmodels] = useState<string[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [modes, setModes] = useState<any[]>([]);
  const [selectedMode, setSelectedMode] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedLevel, setSelectedLevel] = useState('');
  const [levels, setLevels] = useState<any[]>([]);
  const { toast } = useToast();

  // Fetch version on mount
  useEffect(() => {
    setVersion('1.9.1'); // Hardcoded for now, replace with actual API call
  }, []);

  // Fetch categories for navigation
  useEffect(() => {
    const mockCategories = [
      { ref: 'ai_chat', name: 'Chat Socrate' },
      { ref: 'process_keywords', name: 'Keywords' },
      { ref: 'process_synonyms', name: 'Synonyms' },
      { ref: 'process_clusters', name: 'Clusters Analysis' },
      { ref: 'process_clusters_zero', name: 'Clusters Zero Analysis' },
      { ref: 'prompts', name: 'Gestion des prompts' },
      { ref: 'logs', name: 'Logs' }
    ];
    setCategories(mockCategories);
  }, []);

  // Fetch models
  useEffect(() => {
    const mockModels = [
      { model_id: 1, model_name: 'GPT-4' },
      { model_id: 2, model_name: 'Claude' },
      { model_id: 3, model_name: 'Gemini' }
    ];
    setModels(mockModels);
  }, []);

  // Fetch submodels when model changes
  useEffect(() => {
    if (selectedModel) {
      const mockSubmodels = ['Standard', 'Turbo', 'Advanced'];
      setSubmodels(mockSubmodels);
    } else {
      setSubmodels([]);
      setSelectedSubmodel('');
    }
  }, [selectedModel, setSelectedSubmodel]);

  // Fetch modes for cluster pages
  useEffect(() => {
    if (activePage === 'process_clusters' || activePage === 'process_clusters_zero') {
      const mockModes = [
        { ref: 'mode1', name: 'Mode Standard' },
        { ref: 'mode2', name: 'Mode Avancé' }
      ];
      setModes(mockModes);
    }
  }, [activePage]);

  // Fetch levels for prompts
  useEffect(() => {
    if (activePage === 'prompts') {
      const mockLevels = [
        { ref: 'beginner', name: 'Débutant' },
        { ref: 'intermediate', name: 'Intermédiaire' },
        { ref: 'advanced', name: 'Avancé' }
      ];
      setLevels(mockLevels);
    }
  }, [activePage]);

  const showModelSelection = ['ai_chat', 'process_keywords', 'process_synonyms', 'process_clusters', 'process_clusters_zero'].includes(activePage);
  const showFileUpload = ['process_clusters', 'process_clusters_zero'].includes(activePage);
  const showModeSelection = ['process_clusters', 'process_clusters_zero'].includes(activePage);
  const showPromptControls = activePage === 'prompts';

  return (
    <div className="w-80 bg-card border-r border-border h-screen overflow-y-auto p-6">
      {/* Logo and Version */}
      <div className="mb-8 text-center">
        <div className="flex items-center justify-center mb-4">
          <div className="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-xl">S</span>
          </div>
          <h1 className="ml-3 text-xl font-bold text-foreground">SOCRATE</h1>
        </div>
        <p className="text-sm text-muted-foreground">Version : {version}</p>
      </div>

      {/* Mode Selection for Cluster pages */}
      {showModeSelection && (
        <Card className="mb-6">
          <CardContent className="p-4">
            <Label htmlFor="mode-select" className="text-sm font-medium">Mode</Label>
            <Select value={selectedMode} onValueChange={setSelectedMode}>
              <SelectTrigger id="mode-select" className="mt-2">
                <SelectValue placeholder="-- Sélectionner un mode --" />
              </SelectTrigger>
              <SelectContent>
                {modes.map((mode) => (
                  <SelectItem key={mode.ref} value={mode.ref}>
                    {mode.name}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </CardContent>
        </Card>
      )}

      {/* Navigation Menu */}
      <Card className="mb-6">
        <CardContent className="p-4">
          <Label className="text-sm font-medium mb-3 block">Menu</Label>
          <nav className="space-y-2">
            {categories.map((category) => (
              <Button
                key={category.ref}
                variant={activePage === category.ref ? "default" : "ghost"}
                className="w-full justify-start"
                onClick={() => setActivePage(category.ref)}
              >
                {category.name}
              </Button>
            ))}
          </nav>
        </CardContent>
      </Card>

      {/* Model Selection */}
      {showModelSelection && (
        <Card className="mb-6">
          <CardContent className="p-4">
            <div className="space-y-4">
              <div>
                <Label htmlFor="model-select" className="text-sm font-medium">Choisissez un modèle</Label>
                <Select value={selectedModel} onValueChange={setSelectedModel}>
                  <SelectTrigger id="model-select" className="mt-2">
                    <SelectValue placeholder="-- Sélectionner --" />
                  </SelectTrigger>
                  <SelectContent>
                    {models.map((model) => (
                      <SelectItem key={model.model_id} value={model.model_id.toString()}>
                        {model.model_name}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div>
                <Label htmlFor="submodel-select" className="text-sm font-medium">Choisissez un sous modèle</Label>
                <Select value={selectedSubmodel} onValueChange={setSelectedSubmodel} disabled={!selectedModel}>
                  <SelectTrigger id="submodel-select" className="mt-2">
                    <SelectValue placeholder="-- Sélectionner --" />
                  </SelectTrigger>
                  <SelectContent>
                    {submodels.map((submodel) => (
                      <SelectItem key={submodel} value={submodel}>
                        {submodel}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Science Selection */}
      {showModelSelection && (
        <Card className="mb-6">
          <CardContent className="p-4">
            <Label htmlFor="science-select" className="text-sm font-medium">Science</Label>
            <Select value={selectedScience} onValueChange={setSelectedScience}>
              <SelectTrigger id="science-select" className="mt-2">
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="datasocial">Social sciences</SelectItem>
                <SelectItem value="datahealth">Health sciences</SelectItem>
                <SelectItem value="dataengi">Engineering sciences</SelectItem>
              </SelectContent>
            </Select>
          </CardContent>
        </Card>
      )}

      {/* Prompt Controls */}
      {showPromptControls && (
        <>
          <Card className="mb-6">
            <CardContent className="p-4">
              <Label htmlFor="category-select" className="text-sm font-medium">Catégories</Label>
              <Select value={selectedCategory} onValueChange={setSelectedCategory}>
                <SelectTrigger id="category-select" className="mt-2">
                  <SelectValue placeholder="-- Sélectionner une catégorie --" />
                </SelectTrigger>
                <SelectContent>
                  {categories.map((category) => (
                    <SelectItem key={category.ref} value={category.ref}>
                      {category.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </CardContent>
          </Card>

          <Card className="mb-6">
            <CardContent className="p-4">
              <Label htmlFor="level-select" className="text-sm font-medium">Level</Label>
              <Select value={selectedLevel} onValueChange={setSelectedLevel}>
                <SelectTrigger id="level-select" className="mt-2">
                  <SelectValue placeholder="-- Sélectionner un niveau --" />
                </SelectTrigger>
                <SelectContent>
                  {levels.map((level) => (
                    <SelectItem key={level.ref} value={level.ref}>
                      {level.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </CardContent>
          </Card>
        </>
      )}

      {/* File Upload */}
      {showFileUpload && (
        <Card className="mb-6">
          <CardContent className="p-4">
            <Label className="text-sm font-medium mb-3 block">
              Chargez votre fichier Excel (.xlsx)
            </Label>
            <FileUpload 
              activePage={activePage}
              selectedModel={selectedModel}
              selectedSubmodel={selectedSubmodel}
              selectedScience={selectedScience}
            />
          </CardContent>
        </Card>
      )}

      {/* Action Buttons */}
      <div className="space-y-3 mt-8">
        <Button variant="outline" className="w-full bg-blue-600 text-white hover:bg-blue-700">
          Créer un compte
        </Button>
        <Button variant="outline" className="w-full bg-blue-600 text-white hover:bg-blue-700">
          Gestion des prompts
        </Button>
      </div>
    </div>
  );
};

export default Sidebar;

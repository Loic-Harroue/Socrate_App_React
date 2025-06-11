
import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Link } from 'react-router-dom';

const RegisterPage = () => {
  const [isLoading, setIsLoading] = useState(false);

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

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    const formData = new FormData(e.target as HTMLFormElement);
    formData.append('csrfmiddlewaretoken', getCookie('csrftoken') || '');

    try {
      const response = await fetch('/register/', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        // Redirect to main app on successful registration
        window.location.href = '/ai_chat/';
      } else {
        alert('Erreur lors de la création du compte.');
      }
    } catch (error) {
      console.error('Erreur de création de compte:', error);
      alert('Une erreur est survenue lors de la création du compte.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center">
          <CardTitle className="text-2xl font-bold text-gray-900">Créer un compte</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-2">
              <label htmlFor="username" className="text-sm font-medium text-gray-700">
                Nom d'utilisateur
              </label>
              <Input
                id="username"
                name="username"
                type="text"
                required
                className="w-full"
              />
            </div>

            <div className="space-y-2">
              <label htmlFor="email" className="text-sm font-medium text-gray-700">
                Email
              </label>
              <Input
                id="email"
                name="email"
                type="email"
                required
                className="w-full"
              />
            </div>

            <div className="space-y-2">
              <label htmlFor="password1" className="text-sm font-medium text-gray-700">
                Mot de passe
              </label>
              <Input
                id="password1"
                name="password1"
                type="password"
                required
                className="w-full"
              />
            </div>

            <div className="space-y-2">
              <label htmlFor="password2" className="text-sm font-medium text-gray-700">
                Confirmer le mot de passe
              </label>
              <Input
                id="password2"
                name="password2"
                type="password"
                required
                className="w-full"
              />
            </div>

            <Button
              type="submit"
              disabled={isLoading}
              className="w-full bg-blue-600 hover:bg-blue-700"
            >
              {isLoading ? 'Création...' : "S'inscrire"}
            </Button>
          </form>

          <p className="mt-4 text-center text-sm text-gray-600">
            Déjà un compte ?{' '}
            <Link to="/login" className="text-blue-600 hover:text-blue-500">
              Se connecter
            </Link>
          </p>
        </CardContent>
      </Card>
    </div>
  );
};

export default RegisterPage;

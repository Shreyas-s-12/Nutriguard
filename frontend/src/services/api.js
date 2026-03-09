import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

const api = axios.create({
  baseURL: API_URL
});

// Analyze food using FormData (multilingual support)
export const analyzeFood = async (ingredients, language = 'auto') => {
  const formData = new FormData();
  formData.append('ingredients', ingredients);
  formData.append('language', language);
  
  const response = await api.post('/analyze', formData);
  return response.data;
};

// Analyze nutrition facts text
export const analyzeNutrition = async (nutritionText) => {
  const response = await api.post('/analyze-nutrition', {
    nutrition_text: nutritionText
  });

  return response.data;
};

// Comprehensive food analysis using database-driven detection (legacy)
export const analyzeFoodLegacy = async (ingredients, nutritionText = '') => {
  const response = await api.post('/analyze-food', {
    ingredients: ingredients,
    nutrition_text: nutritionText
  });

  return response.data;
};

export const getChemicals = async (search = '', riskLevel = '', category = '', limit = 100) => {
  const params = new URLSearchParams();
  
  if (search) params.append('search', search);
  if (riskLevel && riskLevel !== 'all') params.append('risk_level', riskLevel);
  if (category && category !== 'all') params.append('category', category);
  params.append('limit', limit.toString());
  
  const response = await api.get(`/chemicals?${params.toString()}`);
  return response.data;
};

export default api;

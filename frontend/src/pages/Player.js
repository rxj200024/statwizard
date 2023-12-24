import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
// import Luka from '../../src/images/Luka-Doncic.png'
import { useNavigate, useParams } from 'react-router-dom';
import { API } from '../backend';
// import Luka from '../../public/Luka-Doncic.png'


const Player = ({ firstName, lastName }) => {
  const [averages, setAverages] = useState(null);
  const [predictions, setPredictions] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const navigate = useNavigate();
  const { id } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const apiURL = process.env.BACKEND_AVERAGES_API_URL
        const response = await fetch(`${API}averages/nba/player/${id}`);

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json()

        setAverages(data);
        console.log(`${data.id}-${data.last}`)
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const apiURL = process.env.BACKEND_AVERAGES_API_URL
        const response = await fetch(`${API}predictor/nba/player/${id}`);

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        setPredictions(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <Header/>
      <div className="h-screen">
        <div style={{ backgroundColor: '#ABABAB' }}  className="h-[35%] grid grid-cols-3 border-x-1.5 border-y-2 border-black">
          <div className='col-span-2' >
            <div>
              {loading && <p>Loading...</p>}
              {error && <p>Error: {error}</p>}
              {averages && (
              <div style={{ marginLeft: '20px'}} className='grid grid-rows-4 flex justify-left'>
                <div className='row-span-2 font-serif text-5xl p-6 italic'>
                  <h1>{averages.first} {averages.last}</h1>
                </div>
                <div className='font-serif text-3xl'>
                <h1>Season 2023-2024</h1>
                </div>
                <div className='font-serif text-xl'>
                <pre style={{ fontFamily: 'monospace', margin: 0 }}>
  PTS   REB   AST   STL   BLK   TOV<br/>
  {averages.pts.toFixed(1).padStart(0)}   {averages.reb.toFixed(1).padStart(0)}   {averages.ast.toFixed(1).padStart(0)}   {averages.stl.toFixed(1).padStart(0)}   {averages.blk.toFixed(1).padStart(0)}   {averages.tov.toFixed(1).padStart(0)}
</pre>
                </div>
              </div>)}
            </div>
          </div>
          {averages && (
          <div className="overflow-hidden">
            <img src={`https://cdn.nba.com/headshots/nba/latest/1040x760/${averages.id}.png`} className="max-w-full h-auto"/>
          </div>
          )}
        </div>
        <div className="h-[65%] flex items-center justify-center h-full">
        {loading && <p>Loading...</p>}
        {error && <p>Error: {error}</p>}
        {predictions && (
          <div style={{ backgroundColor: '#D9D9D9', boxShadow: '2px 2px 2px 2px rgb(156 163 175)' }} className='sm:w-2/3 md:w-1/2 lg:w-1/3 xl:w-2/5 h-3/5 border-2 border-solid p-4 border-gray-500 font-thin'>
            <h1 style={{fontFamily: 'Courier New'}} className="text-lg md:text-xl lg:text-3xl xl:text-5xl text-center font-thin">Predictions</h1><br/><br/>
            <pre className="text-sm md:text-lg lg:text-xl xl:text-4xl" style={{fontFamily: 'Courier New'}}>
              Points      {predictions.pts.toFixed(1)}<br/>
              Rebounds    {predictions.reb.toFixed(1)}<br/>
              Assists     {predictions.ast.toFixed(1)}<br/>
              Steals      {predictions.stl.toFixed(1)}<br/>
              Blocks      {predictions.blk.toFixed(1)}<br/>
              Turnovers   {predictions.tov.toFixed(1)}
            </pre>
          </div>
        )}
        </div>
      </div>
      <Footer/>
    </div>
  );
};

export default Player;


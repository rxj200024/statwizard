import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { API } from '../backend';


const PlayerDropdown = () => {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    // Fetch the list of active NBA players from your API
    const fetchPlayers = async () => {
      try {
        const response = await fetch(`${API}players/`);
        const data = await response.json();
        console.log(data.data)
        setPlayers(data.data);
      } catch (error) {
        console.error('Error fetching players', error);
      }
    };

    fetchPlayers();
  }, []);

  return (
    <div style={{ backgroundColor: '#D9D9D9', boxShadow: '2px 2px 2px 2px rgb(156 163 175)' }}
    className='sm:w-2/3 md:w-1/2 lg:w-1/3 xl:w-1/4 flex flex-col items-center justify-center border bg-gray-200 border-gray-300 rounded mt-2 p-20'>
      <label style={{ color: '#33423A', }} htmlFor="playerDropdown" className='font-serif text-2xl mb-5'>statwizard</label>
      <select id="playerDropdown">
        <option value="" disabled selected>
          Choose a Player
        </option>
        {players.map((player) => (
          <option key={player.id} value={player.id}>
            {player.full_name}
          </option>
        ))}
      </select>
      <button style={{ backgroundColor: '#33424A', hover: '#33424A', color: 'white'}} className="mt-10 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700"
        onClick={() => {
          const selectedPlayerId = document.getElementById('playerDropdown').value;
          if (selectedPlayerId) {
            window.location.href = `http://localhost:3000/player/${selectedPlayerId}`;
          }
        }}
      >
        Go to Player
      </button>
    </div>
  );
};

export default PlayerDropdown;
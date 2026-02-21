import React,  { useState, useCallback } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import MainTabs from './components/MainTabs';

function App() {
    const [currentTrack, setCurrentTrack] = useState(null);
    const [currentPlaylist, setCurrentPlaylist] = useState([]);

    const handleTrackPlay = (track) => {
      setCurrentTrack(track);
    }
  

  return (
    <div>
      <MainTabs 
        onTrackPlay={handleTrackPlay}
        currentTrack={currentTrack}
        setCurrentPlaylist={setCurrentPlaylist}
      />
    </div>
  );
}

export default App;

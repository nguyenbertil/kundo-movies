import { Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage";
import MoviePage from "./pages/MoviePage";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/movie/:imdbID" element={<MoviePage />} />
      </Routes>
    </div>
  );
}

export default App;

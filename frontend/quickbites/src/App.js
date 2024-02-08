import './App.css';
import Home from './components/Home';
import Categories from './components/Categories';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import "bootstrap/dist/css/bootstrap.min.css";
import NavBar from './components/Navbar';
import Item from './components/Item';
import Footer from './components/Footer';
function App() {
  return (
    <div className="App">
      
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/item" element={<Item />} />
          <Route path="/categories" element={<Categories />} />
        </Routes>
        <Footer />
    </div>
  );
}

export default App;


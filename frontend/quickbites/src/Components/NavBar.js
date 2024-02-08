// NavBar.js
import React, { useState, useEffect } from 'react';
import { useCart } from 'react-use-cart';

function NavBar({ onCategoryChange, onSearch }) {
  const [selectedCategory, setSelectedCategory] = useState('');
  const [products, setProducts] = useState([]);
  const [searchedProduct, setSearchedProduct] = useState('');
  const [isMobileMenuOpen, setMobileMenuOpen] = useState(false);
  const { totalItems } = useCart();
  const [cartHasItems, setCartHasItems] = useState(false);

  useEffect(() => {
    // Fetch data from the local server
    fetch('https://my-json-server.typicode.com/leon-kxng/Munchies/foods')
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  useEffect(() => {
    setCartHasItems(totalItems > 0);
  }, [totalItems]);

  const uniqueCategories = products ? [...new Set(products.map((product) => product.category))] : [];

  const handleCategoryChange = (e) => {
    const selectedValue = e.target.value;
    setSelectedCategory(selectedValue);
    onCategoryChange(selectedValue);
  };

  const handleSearchInput = (e) => {
    const inputText = e.target.value;
    setSearchedProduct(inputText);
    onSearch(inputText);
  };

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!isMobileMenuOpen);
  };

  const categoryList = (
    <select onChange={handleCategoryChange} value={selectedCategory} className="category-dropdown">
      <option value=''>Categories</option>
      {uniqueCategories.map((category) => (
        <option key={category} value={category}>
          {category}
        </option>
      ))}
    </select>
  );

  return (
    <nav className="navbar">
      <div className="container-fluid">
        <button
          className="navbar-toggler"
          type="button"
          onClick={toggleMobileMenu}
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className={`navbar-collapse ${isMobileMenuOpen ? 'show-mobile' : 'pc-view'}`}>
          <ul className="navbar-nav">
            <li className="nav-item home">
              <a className="nav-link active" href="/">
                Menu
              </a>
            </li>
            <li className="nav-item cart">
              <a className="nav-link active" href="/cart">
                Checkout {cartHasItems && <span className="dot"></span>}
              </a>
            </li>
          </ul>

          <form className="d-flex search">
            <div className={`search-and-category ${isMobileMenuOpen ? 'show-on-mobile' : ''}`}>
              <input
                className="form-control me-2 search-input search"
                type="search"
                placeholder="Search food"
                aria-label="Search"
                onChange={handleSearchInput}
                value={searchedProduct}
              />
              {categoryList}
            </div>
          </form>
        </div>
      </div>
    </nav>
  );
}

export default NavBar;


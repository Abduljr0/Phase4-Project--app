import React, { useState } from 'react';
import { useCart } from 'react-use-cart';

function Menu({ products }) {
  const { addItem, removeItem, inCart } = useCart();

  const [expanded, setExpanded] = useState({});

  const toggleDescription = (id) => {
    setExpanded((prevExpanded) => ({
      ...prevExpanded,
      [id]: !prevExpanded[id],
    }));
  };

  const handleClick = (product) => {
    if (inCart(product.id)) {
      removeItem(product.id);
    } else {
      addItem(product);
    }
  };

  return (
    <div className='container'>
      {/* Add container class and set padding on the sides */}
      <div className='row'>
        {products.map((product) => (
          <div className='col-md-4 mb-4' key={product.id}>
            {/* Use 'col-md-4' to make each card take up one-third of the container's width */}
            <div className='card h-100'>
              <img
                src={product.image}
                className='card-img-top'
                alt='Product'
                style={{ height: '250px', objectFit: 'cover' }}
              />
              <div className='card-body d-flex flex-column'>
                <h5 className='card-title'>{product.name}</h5>
                <h6 className='card-title'>{product.category.toUpperCase()}</h6>
                <p className='card-text flex-grow-1'>
                  {expanded[product.id]
                    ? product.description
                    : `${product.description.slice(0, 100)}...`}
                </p>
                {product.description.length > 100 && (
                  <button
                    className='btn btn-link mt-auto'
                    onClick={() => toggleDescription(product.id)}
                  >
                    {expanded[product.id] ? 'Read Less' : 'Read More'}
                  </button>
                )}
                <p className='card-text'>Price: ${product.price}</p>

                <button
                  className={inCart(product.id) ? 'btn btn-danger' : 'btn btn-primary'}
                  onClick={() => handleClick(product)}
                >
                  {inCart(product.id) ? 'Remove order' : 'Order Now'}
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Menu;

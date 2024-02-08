import React from "react";
import { useCart } from "react-use-cart";

function handleOrder() {
  // Make an AJAX request to fetch the driver's name from the server
  fetch('/get_driver_name')
      .then(response => response.json())
      .then(data => {
          const driverName = data.driver_name || 'Unknown';
          // Display an alert indicating that the order is being processed
          alert(`Your order is being processed and will be delivered by ${driverName}`);
      })
      .catch(error => {
          console.error('Error:', error);
      });
}

const Cart = () => {
  const {
    isEmpty,
    totalUniqueItems,
    items,
    totalItems,
    cartTotal,
    updateItemQuantity,
    removeItem,
    emptyCart,
  } = useCart();

  if (isEmpty) return <h1>Your Cart is Empty</h1>;

  return (
    <section style={{ backgroundColor: 'rgb(80, 125, 141)' }}>
      <div>
        <div>
          <h5>Cart ({totalUniqueItems}) total Items: ({totalItems})</h5>
          <table>
            <tbody>
              {items.map((item, index) => {
                return (
                  <tr key={index}>
                    <td>
                      <img src={item.image} alt={item.title} style={{ height: '6rem' }} />
                    </td>
                    <td>{item.title}</td>
                    <td>{item.price.toLocaleString('en-US', { style: 'currency', currency: 'USD' })}</td>
                    <td>Quantity ({item.quantity})</td>
                    <td>
                      <button
                        onClick={() => updateItemQuantity(item.id, item.quantity - 1)}
                      >-</button>
                      <button
                        onClick={() => updateItemQuantity(item.id, item.quantity + 1)}
                      >+</button>
                      <button  type="button" class="btn btn-primary"
                        onClick={() => removeItem(item.id)}
                      >Remove Item</button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
        <div>
          <h2>Total : {cartTotal.toLocaleString('en-US', { style: 'currency', currency: 'USD' })}</h2>
        </div>
        <div>
          <button
            onClick={() => window.confirm("Are you sure you want to clear the cart?") && emptyCart()}
          >Clear Cart</button>
          <button type="button" class="btn btn-success" onClick={() => window.confirm("your order is being processed and will be delivered  soon Thank you!")} >Buy Now</button>
        </div>
      </div>
    </section>
  );
};

export default Cart;

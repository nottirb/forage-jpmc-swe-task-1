import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    expected_results = [
      ('ABC', 120.48, 121.2, 120.84),
      ('DEF', 117.87, 121.68, 119.775)
    ]
    
    for i, quote in enumerate(quotes):
      with self.subTest(i = i):
          result = getDataPoint(quote)
          self.assertEqual(result, expected_results[i])

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    expected_results = [
        ('ABC', 120.48, 119.2, 119.84),
        ('DEF', 117.87, 121.68, 119.775)
    ]
    
    for i, quote in enumerate(quotes):
      with self.subTest(i=i):
        result = getDataPoint(quote)
        self.assertEqual(result, expected_results[i])
        
  def test_getDataPoint_calculatePriceBidEqualAsk(self):
    quotes = [ 
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.2, 'size': 36}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.5, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.5, 'size': 4}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    expected_results = [
        ('ABC', 119.2, 119.2, 119.2),
        ('DEF', 121.5, 121.5, 121.5)
    ]
    
    for i, quote in enumerate(quotes):
      with self.subTest(i=i):
        result = getDataPoint(quote)
        self.assertEqual(result, expected_results[i])
    
  def test_getRatio(self):
    test_cases = [
      (30.0, 20.0, 1.5),
      (20.0, 30.0, 2/3),
      (10.0, 10.0, 1.0),
      (0.0, 10.0, 0.0),
      (10.0, 0.0, None)  # Division by zero case
    ]

    for i, (price_a, price_b, expected) in enumerate(test_cases):
      with self.subTest(i=i):
        result = getRatio(price_a, price_b)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

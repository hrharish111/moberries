from django.urls import reverse

from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase

from .factories import (
    PizzaSizeFactory,
    HawaiianPizzaFactory,
    HawaiianSize30Factory,
    PizzaFactory,
)


class TestPizzaSize(APITestCase):
    """
    Test cases for :model:`product.PizzaSize`
    """

    def setUp(self):
        self.size = PizzaSizeFactory(size=60)
        self.payload = {
            'size': 70
        }
        self.url = reverse('pizzasize-list')
        self.detail_url = reverse(
            'pizzasize-detail',
            kwargs={'pk': self.size.pk}
        )

    def test_get_pizza_sizes_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_pizza_size_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_pizza_size(self):
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_pizza_size(self):
        payload = {
            "size": 80
        }
        response = self.client.put(self.detail_url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_pizza_size(self):
        response = self.client.delete(self.detail_url, {})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestPizza(APITestCase):
    """
    Test cases for :model:`product.Pizza`
    """
    def setUp(self):
        self.pizza = HawaiianPizzaFactory()
        self.payload = {
            'name': "Pepperoni"
        }
        self.url = reverse('pizza-list')
        self.detail_url = reverse(
            'pizza-detail',
            kwargs={'pk': self.pizza.pk}
        )

    def test_get_pizza_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_pizza_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_pizza(self):
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_pizza(self):
        payload = {
            "name": "Hawaiian Supreme"
        }
        response = self.client.put(self.detail_url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_pizza(self):
        response = self.client.delete(self.detail_url, {})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestPizzaVariation(APITestCase):
    """
    Test cases for :model:`product.PizzaVariation`
    """
    def setUp(self):
        self.variation = HawaiianSize30Factory()
        pizza = PizzaFactory(name="Mac and Cheese")
        size30 = PizzaSizeFactory(size=30)
        self.payload = {
            'pizza': pizza.pk,
            'size': size30.pk,
            'price': Decimal('10.99'),
        }
        self.url = reverse('pizzavariation-list')
        self.detail_url = reverse(
            'pizzavariation-detail',
            kwargs={'pk': self.variation.pk}
        )

    def test_get_pizza_variation_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_pizza_variation_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_pizza_variation(self):
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_pizza_variation(self):
        payload = {
            "price": Decimal('9.99')
        }
        response = self.client.put(self.detail_url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_pizza_variation(self):
        response = self.client.delete(self.detail_url, {})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

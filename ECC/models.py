from django.db import models
from django.contrib.auth.models import User

# Usuarios

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True, db_column="idGenero")
    genero = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.genero


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(
        "Genero", on_delete=models.CASCADE, db_column="IDGenero"
    )
    telefono = models.CharField(max_length=12)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField()

    def __str__(self):
        return (self.rut)+ " "+(self.nombre)+ " "+ (self.apellido_paterno)+ " "+ (self.apellido_materno)


#Productos

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	

#Peleadores

class Categoria(models.Model):
	id_categoria = models.AutoField(primary_key=True, db_column="idCategoria")
	categoria = models.CharField(max_length=25, blank=False, null=False)

	def __str__(self):
		return str(self.categoria)

class Peleador(models.Model):
	nom_peleador = models.CharField(max_length=200)
	id_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
	victoria = models.IntegerField()
	derrota = models.IntegerField()
	empate = models.IntegerField()
	altura = models.FloatField()
	peso = models.FloatField()
	descripcion = models.CharField(max_length=300)
	imag_peleador = models.ImageField(null=True, blank=True)

	def __str__(self):
		return str(self.nom_peleador)
	
	@property
	def imageURL(self):
		try:
			url = self.imag_peleador.url
		except:
			url = ''
		return url
	
	@property
	def puntos_totales(self):
		puntos_totales = (self.victoria * 100) + (self.empate * 50) - (self.derrota * 50)
		return puntos_totales
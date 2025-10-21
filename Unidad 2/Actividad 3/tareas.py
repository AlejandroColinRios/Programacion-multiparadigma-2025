import json
from datetime import datetime

# CLASE BASE: Tarea 
class Tarea:
    """Clase base para representar una tarea"""
    
    def __init__(self, titulo, descripcion, prioridad="Media"):
        # Atributos privados
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__completada = False
        self.__fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Propiedades 
    @property
    def titulo(self):
        return self.__titulo

    @property
    def prioridad(self):
        return self.__prioridad

    @property
    def completada(self):
        return self.__completada
    
    # Setter para modificar el estado de completado
    @completada.setter
    def completada(self, estado):
        if isinstance(estado, bool):
            self.__completada = estado
        else:
            raise ValueError("El estado debe ser booleano")

    # Polimorfismo: Metodo base para mostrar informacion
    def mostrar_info(self):
        """Muestra la informacion basica de la tarea"""
        estado = "Completada" if self.__completada else "Pendiente"
        return f"Titulo: {self.__titulo} | Prioridad: {self.__prioridad} | Estado: {estado} | Creada: {self.__fecha_creacion}"
    
    # Metodo para serializar el objeto a diccionario 
    def to_dict(self):
        """Convierte la tarea a un diccionario serializable"""
        return {
            "clase": self.__class__.__name__,
            "titulo": self.__titulo,
            "descripcion": self.__descripcion,
            "prioridad": self.__prioridad,
            "completada": self.__completada,
            "fecha_creacion": self.__fecha_creacion
        }

# CLASES DERIVADAS (Herencia y Polimorfismo)

class TareaUrgente(Tarea):
    """Representa una tarea con prioridad alta y fecha limite"""
    
    def __init__(self, titulo, descripcion, fecha_limite):
        # Herencia
        super().__init__(titulo, descripcion, prioridad="ALTA")
        self.__fecha_limite = fecha_limite

    # Polimorfismo: Redefinicion del metodo mostrar_info()
    def mostrar_info(self):
        """Muestra la informacion de la tarea urgente con la fecha limite"""
        info_base = super().mostrar_info()
        return f"{info_base} | Tipo: Urgente | Limite: {self.__fecha_limite}"

    # Redefinicion de to_dict para incluir el nuevo atributo
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["fecha_limite"] = self.__fecha_limite
        return base_dict

class TareaRecurrente(Tarea):
    """Representa una tarea que se repite"""

    def __init__(self, titulo, descripcion, recurrencia="Diaria"):
        # Herencia
        super().__init__(titulo, descripcion, prioridad="Media")
        self.__recurrencia = recurrencia

    # Polimorfismo: Redefinicion del metodo mostrar_info()
    def mostrar_info(self):
        """Muestra la informacion de la tarea recurrente con el patron de repeticion"""
        info_base = super().mostrar_info()
        return f"{info_base} | Tipo: Recurrente | Repeticion: {self.__recurrencia}"

    # Redefinicion de to_dict para incluir el nuevo atributo
    def to_dict(self):
        base_dict = super().to_dict()
        base_dict["recurrencia"] = self.__recurrencia
        return base_dict

# CLASE DE GESTION: GestorTareas
class GestorTareas:
    """Clase para gestionar una coleccion de objetos Tarea y su persistencia"""
    
    def __init__(self, archivo="tareas.json"):
        self.tareas = []
        self.archivo = archivo
        self._cargar_tareas()

    # Metodo estatico para reconstruir objetos
    @staticmethod
    def _crear_objeto_tarea(data):
        """Funcion fabrica para crear instancias de la clase correcta (polimorfismo)"""
        clase = data.pop("clase")
        titulo = data["titulo"]
        descripcion = data["descripcion"]
        completada = data["completada"]
        
        if clase == "TareaUrgente":
            tarea = TareaUrgente(titulo, descripcion, data["fecha_limite"])
        elif clase == "TareaRecurrente":
            tarea = TareaRecurrente(titulo, descripcion, data["recurrencia"])
        else:
            tarea = Tarea(titulo, descripcion, data["prioridad"])

        # Restaurar estado completada (uso del setter encapsulado)
        tarea.completada = completada 
        return tarea

    # Persistencia de Datos (Guardar y Cargar)

    def _cargar_tareas(self):
        """Carga las tareas desde el archivo JSON"""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tareas = [self._crear_objeto_tarea(d) for d in data]
            print(f"Tareas cargadas exitosamente desde {self.archivo}")
        except FileNotFoundError:
            print("Archivo de tareas no encontrado Se inicia con lista vacia")
            self.tareas = []
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON Se inicia con lista vacia")
            self.tareas = []
        except Exception as e:
            print(f"Ocurrio un error al cargar: {e}")
            self.tareas = []

    def _guardar_tareas(self):
        """Guarda las tareas en el archivo JSON"""
        try:
            data = [tarea.to_dict() for tarea in self.tareas]
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"Tareas guardadas exitosamente en {self.archivo}")
            return True
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")
            return False

    # Metodos de Gestion

    def agregar_tarea(self, tarea):
        """Anade un objeto Tarea a la lista"""
        self.tareas.append(tarea)
        print(f"-> Tarea '{tarea.titulo}' agregada")
        self._guardar_tareas()

    def listar_tareas(self):
        """Muestra todas las tareas registradas"""
        if not self.tareas:
            print("No hay tareas registradas")
            return

        print("\n--- LISTA DE TAREAS ---")
        for i, tarea in enumerate(self.tareas):
            # Polimorfismo en accion
            print(f"[{i+1}] {tarea.mostrar_info()}") 
        print("-----------------------\n")

    def marcar_completada(self, indice):
        """Marca una tarea como completada por su indice"""
        try:
            tarea = self.tareas[indice - 1]
            if not tarea.completada:
                # Encapsulacion: Uso del setter
                tarea.completada = True 
                print(f"-> Tarea {indice}: '{tarea.titulo}' marcada como COMPLETADA")
                self._guardar_tareas()
            else:
                print(f"Tarea {indice} ya estaba completada")
        except IndexError:
            print("Indice de tarea no valido")

    def eliminar_tarea(self, indice):
        """Elimina una tarea por su indice"""
        try:
            tarea_eliminada = self.tareas.pop(indice - 1)
            print(f"-> Tarea {indice}: '{tarea_eliminada.titulo}' eliminada")
            self._guardar_tareas()
        except IndexError:
            print("Indice de tarea no valido")
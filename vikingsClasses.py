import random

#  Soldier

class Soldier:
    """
    Clase Soldier: Esta es la clase base para Viking y Saxon.
    """

    def __init__(self, health, strength):
        """
        Constructor:
        - Debe inicializar los atributos:
          - health (int): Nivel de salud del soldado.
          - strength (int): Fuerza del soldado.
        """
        self.health = health
        self.strength = strength

    def attack(self):
        """
        Método attack:
        - Debe devolver el valor de la fuerza del soldado ('strength').
        - No recibe argumentos adicionales.
        """
        return self.strength

    def receiveDamage(self, damage):
        """
        Método receiveDamage:
        - Debe restar el daño recibido del atributo 'health'.
        - No devuelve nada (esta versión base no tiene mensajes).
        """
        self.health -= damage

# Viking

class Viking(Soldier):
    """
    Clase Viking: Hereda de Soldier y añade características únicas.
    """

    def __init__(self, name, health, strength):
        """
        Constructor:
        - Debe inicializar los atributos:
          - name (str): Nombre del vikingo.
          - health (int): Salud del vikingo (heredado de Soldier).
          - strength (int): Fuerza del vikingo (heredado de Soldier).
        """
        self.name = name
        Soldier.__init__(self, health, strength)
        """
        self.name = name
        super().__init__(health, strength)
        """

    def battleCry(self):
        """
        Método battleCry:
        - Debe devolver el mensaje "Odin Owns You All!".
        """
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        """
        Método receiveDamage:
        - Debe reducir la salud según el daño recibido.
        - Si el vikingo sigue vivo, devuelve:
          "{name} has received {damage} points of damage".
        - Si el vikingo muere, devuelve:
          "{name} has died in act of combat".
        """
        if self.health - damage <= 0:
            self.health = 0
            return f"{self.name} has died in act of combat"
        else:
            self.health -= damage
            return f"{self.name} has received {damage} points of damage"


# Saxon

class Saxon(Soldier):
    """
    Clase Saxon: Hereda de Soldier y añade un comportamiento único.
    """

    def __init__(self, health, strength):
        """
        Constructor:
        - Debe inicializar los atributos:
          - health (int): Salud del sajón.
          - strength (int): Fuerza del sajón.
        """
        Soldier.__init__(self, health, strength)
        """
        super().__init__(health, strength)
        """

    def receiveDamage(self, damage):
        """
        Método receiveDamage:
        - Debe restar el daño recibido del atributo 'health'.
        - Si el sajón sigue vivo, devuelve:
          "A Saxon has received {damage} points of damage".
        - Si el sajón muere, devuelve:
          "A Saxon has died in combat".
        """
        if self.health - damage <= 0:
            self.health = 0
            return "A Saxon has died in combat"
        else:
            self.health -= damage
            return f"A Saxon has received {damage} points of damage"


# B O N U S

# War

class War:
    """
    Clase War: Gestiona los ejércitos de vikingos y sajones y las batallas.
    """

    def __init__(self):
        """
        Constructor:
        - Inicializa dos listas vacías:
          - vikingArmy: Lista de vikingos.
          - saxonArmy: Lista de sajones.
        """
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        """
        Método addViking:
        - Recibe un objeto de tipo Viking.
        - Agrega el vikingo a la lista 'vikingArmy'.
        """
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        """
        Método addSaxon:
        - Recibe un objeto de tipo Saxon.
        - Agrega el sajón a la lista 'saxonArmy'.
        """
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        """
        Método vikingAttack:
        - Selecciona un vikingo y un sajón al azar.
        - El vikingo ataca al sajón.
        - Si el sajón muere, se elimina de 'saxonArmy'.
        - Devuelve el resultado del ataque (mensaje de 'receiveDamage').
        """
        viking = self.vikingArmy[0]
        saxon = self.saxonArmy[0]
        if saxon.health == 0:
            self.saxonArmy.remove(saxon)
        return saxon.receiveDamage(viking.attack())

    def saxonAttack(self):
        """
        Método saxonAttack:
        - Selecciona un sajón y un vikingo al azar.
        - El sajón ataca al vikingo.
        - Si el vikingo muere, se elimina de 'vikingArmy'.
        - Devuelve el resultado del ataque (mensaje de 'receiveDamage').
        """
        saxon = self.vikingArmy[0]
        viking = self.saxonArmy[0]
        if viking.health == 0:
            self.vikingArmy.remove(viking)
        return viking.receiveDamage(saxon.attack())

    def showStatus(self):
        """
        Método showStatus:
        - Si no quedan sajones, devuelve:
          "Vikings have won the war of the century!".
        - Si no quedan vikingos, devuelve:
          "Saxons have fought for their lives and survived another day...".
        - Si ambos ejércitos aún tienen soldados, devuelve:
          "Vikings and Saxons are still in the thick of battle.".
        """
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survived another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass



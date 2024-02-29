class CategoryOrderABC(ABC):
    @abstractmethod
    def total_cost(self):
        pass

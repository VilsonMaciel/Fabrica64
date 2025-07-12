from enum import Enum

class TipoUsuario(Enum):
    adm = 1
    professor = 2
        
def role_required(*allowed_roles: TipoUsuario):
    def decorador(func):
        def wrapper(self, *args, **kwargs):
            # Se nenhuma permissão foi especificada, permite qualquer um
            if not allowed_roles:
                return func(self, *args, **kwargs)

            if self.tipo_usuario not in allowed_roles:
                roles = ', '.join(role.value for role in allowed_roles)
                raise PermissionError(f"Acesso negado. Função requer: {roles}.")
            return func(self, *args, **kwargs)
        return wrapper
    return decorador

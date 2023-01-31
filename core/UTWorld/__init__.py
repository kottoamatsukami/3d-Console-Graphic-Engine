from core.UTViewport import ViewPort
from core.UTGeneral import Vector3D


class Body:
    id = 0
    def __init__(self, name="body", cords=Vector3D(0, 0, 0), id=None, render=True):
        self.name = name
        self.cords = cords
        self.render = render
        self.can_link = True
        self.id = self.id + 1 if id is None else id

    def _total_(self) -> int:
        return self.id


class World:
    def __init__(self, name: str) -> None:
        self.name = name
        self.objects = dict()
        self.can_link = True
        self.last_viewport_pos = Vector3D(0, 0, 0)

    def add_body(self, body) -> None:
        if body.can_link:
            self.objects[body.name] = {
                'render' : body.render,
                'cords'  : body.cords,
                'id'     : body.id,
            }
        else:
            raise ValueError(f'Cannot link body! {body}')

    def __repr__(self) -> str:
        return f"World({self.name}) - {len(self.objects)} objects."


class Linker:
    def __init__(self, viewport: ViewPort):
        self.viewport = viewport
        self.linked_worlds = dict()
        self.cur_world = None

    def link_world(self, world: World) -> None:
        if world.can_link:
            self.linked_worlds[len(self.linked_worlds)] = {
                'name' : world.name,
                'world': world,
            }
        else:
            raise ValueError(f'Cannot link world! {world}')

    def delete_world(self, id) -> bool:
        if isinstance(id, int):
            try:
                self.linked_worlds.pop(id)
                self.refactor_worlds()
                return True
            except:
                raise ValueError(f'Cannot delete world! {id}')

        elif isinstance(id, str):
            for key in self.linked_worlds.keys():
                if self.linked_worlds[key]['name'] == id:
                    self.linked_worlds.pop(key)
                    self.refactor_worlds()
                    return True
            return False

        else:
            raise ValueError(f'Invalid id: {id}! Use world_name or world_id in linker.')

    def refactor_worlds(self) -> None:
        foo = self.linked_worlds.copy()
        self.linked_worlds.clear()
        for _ in range(len(foo)):
            self.link_world(foo['world'])

    def get_world(self, id: (str, int)) -> World:
        if isinstance(id, int):
            try:
                return self.linked_worlds[id]['world']
            except:
                raise ValueError(f'Cannot get world! {id}')

        elif isinstance(id, str):
            for key in self.linked_worlds.keys():
                if self.linked_worlds[key]['name'] == id:
                    return self.linked_worlds[key]['world']
            raise ValueError(f'Cannot get world! {id}')

    def load_world(self, id: (str, int)):
        self.cur_world = self.get_world(id)

    def add_body_to_cur_world(self, body) -> None:
        if self.cur_world is not None:
            self.cur_world.add_body(body)
        else:
            raise ValueError(f'Cannot add body to world! {body} {self.cur_world}')

    def render_scene(self) -> None:
        pass
    def clear_scene(self) -> None:
        pass

    def __repr__(self) -> str:
        out = f"Linker: {len(self.linked_worlds)} worlds loaded:\n"
        for i in range(len(self.linked_worlds)):
            out += f"\t{i} --> {self.linked_worlds[i]['name']} {'<current>' if self.get_world(i) == self.cur_world else ''}\n"
        return out
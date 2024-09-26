from assets.asset import Asset

class Assethandler:

    assets: list[Asset]

    def __init__(self) -> None:
        self.assets = []

    def register(self, asset: any):
        self.assets.append(asset)

    def get_assets_with_tag(self, tag: str):
        return [asset for asset in self.assets if asset.TAG == tag]
    
    def get_assets_to_render(self) -> list[Asset]:
        return [asset for asset in self.assets if asset.RENDER]
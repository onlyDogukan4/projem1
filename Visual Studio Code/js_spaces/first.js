var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);

function preload() {
    // Oyun içinde kullanılacak olan kaynakları yükleyin
}

function create() {
    // Oyun nesnelerini oluşturun
}

function update() {
    // Oyun durumu güncelleyin
}

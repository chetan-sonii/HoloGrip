(() => {
    const mount = document.getElementById("scene");

    if (!mount || typeof THREE === "undefined") return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, mount.clientWidth / mount.clientHeight, 0.1, 100);
    camera.position.set(0, 1.2, 5.2);

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(mount.clientWidth, mount.clientHeight);
    mount.appendChild(renderer.domElement);

    scene.add(new THREE.AmbientLight(0xffffff, 1.7));

    const keyLight = new THREE.DirectionalLight(0xffffff, 2.4);
    keyLight.position.set(4, 5, 5);
    scene.add(keyLight);

    const fillLight = new THREE.DirectionalLight(0x93c5fd, 1.2);
    fillLight.position.set(-4, 2, 1);
    scene.add(fillLight);

    const bodyGeometry = new THREE.BoxGeometry(2.15, 0.7, 1.5);
    const bodyMaterial = new THREE.MeshStandardMaterial({
        color: 0x3b82f6,
        metalness: 0.3,
        roughness: 0.32,
    });

    const body = new THREE.Mesh(bodyGeometry, bodyMaterial);
    scene.add(body);

    const edges = new THREE.LineSegments(
        new THREE.EdgesGeometry(bodyGeometry),
        new THREE.LineBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.9 })
    );
    body.add(edges);

    const sensorGeometry = new THREE.CylinderGeometry(0.25, 0.25, 0.12, 32);
    const sensorMaterial = new THREE.MeshStandardMaterial({ color: 0x0f172a, metalness: 0.75, roughness: 0.25 });
    const sensor = new THREE.Mesh(sensorGeometry, sensorMaterial);
    sensor.rotation.x = Math.PI / 2;
    sensor.position.set(0, 0.41, 0);
    body.add(sensor);

    const grid = new THREE.GridHelper(7, 14, 0x334155, 0x1e293b);
    grid.position.y = -0.85;
    scene.add(grid);

    const target = { roll: 0, pitch: 0, yaw: 0 };

    function setOrientation(roll, pitch, yaw) {
        target.roll = THREE.MathUtils.degToRad(Number(roll) || 0);
        target.pitch = THREE.MathUtils.degToRad(Number(pitch) || 0);
        target.yaw = THREE.MathUtils.degToRad(Number(yaw) || 0);
    }

    window.gyroScene = { setOrientation };

    function resize() {
        const width = mount.clientWidth;
        const height = mount.clientHeight;

        if (!width || !height) return;

        camera.aspect = width / height;
        camera.updateProjectionMatrix();
        renderer.setSize(width, height);
    }

    window.addEventListener("resize", resize);

    function animate() {
        requestAnimationFrame(animate);

        body.rotation.x += (target.pitch - body.rotation.x) * 0.10;
        body.rotation.y += (target.yaw - body.rotation.y) * 0.10;
        body.rotation.z += (target.roll - body.rotation.z) * 0.10;

        renderer.render(scene, camera);
    }

    resize();
    animate();
})();

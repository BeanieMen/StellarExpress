pacman -Syu --noconfirm && pacman -S --noconfirm base-devel git sudo wget python-pip


mkdir -p /tmp/yay-build
useradd -m -G wheel builder && passwd -d builder
chown -R builder:builder /tmp/yay-build
echo 'builder ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
su - builder -c "git clone https://aur.archlinux.org/yay.git /tmp/yay-build/yay"
su - builder -c "cd /tmp/yay-build/yay && makepkg -si --noconfirm"
rm -rf /tmp/yay-build
su - builder

pip install astropy --break-system-packages



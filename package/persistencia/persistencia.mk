PERSISTENCIA_SITE = $(TOPDIR)/package/persistencia
PERSISTENCIA_INSTALL_TARGET = YES

define PERSISTENCIA_INSTALL_TARGET_CMDS
    $(INSTALL) -m 0755 $(PERSISTENCIA_SITE)/integracao.py $(TARGET_DIR)/root/
    $(INSTALL) -m 0755 $(PERSISTENCIA_SITE)/inicializacao $(TARGET_DIR)/etc/init.d/
endef

$(eval $(generic-package))

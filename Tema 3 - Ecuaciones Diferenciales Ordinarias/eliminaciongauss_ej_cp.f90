	PROGRAM eliminagauss

	DIMENSION A(10,11)
	PRINT *
	PRINT *,'Metodo de eliminacion de Gauss'

	DATA N /4/

	DATA (A(1,J), J=1,5) /1.33E-4,4.123E+1, 7.912E+2, -1.544E+3, -711.5698662/
	DATA (A(2,J), J=1,5) /1.77,2.367E-5,2.070E+1,-9.035E+1,-67.87297633/
	DATA (A(3,J), J=1,5) /9.188,0,-1.015E+1,1.988E-4,-0.961801200/
	DATA (A(4,J), J=1,5) /1.002E+2,1.442E+4,-7.014E+2,5.321,13824.12100/

	PRINT *
	PRINT *, 'Matriz aumentada'
	PRINT *

	DO I = 1, N
		PRINT 61, (A(I,J), J=1,4)
61		FORMAT(1X,1P6E12.4)
	END DO

	PRINT *

	CALL GAUSS(N,A)

	PRINT *
	PRINT *, '   SOLUCION   '
	PRINT *, '--------------------------------------'
	PRINT *, '     I     X(I)     '
	PRINT *, '--------------------------------------'

	DO I=1,N
72		FORMAT(5X, I5, 1PE16.6)
		PRINT 72, I, A(I,N+1)
	END DO

	PRINT *, '--------------------------------------'
	PRINT *
	STOP
	END PROGRAM
!++++++++++++++++++++++++++++++++++++++
	SUBROUTINE GAUSS(N,A)
	INTEGER PV
	DIMENSION A(10,11)

	EPS = 1.0
10	IF (1.0 + EPS .GT. 1.0) THEN
		EPS = EPS/2.0
		GOTO 10
	END IF
	
	EPS = EPS*2
	PRINT *, '    EPSILON DE LA MAQUINA = ', EPS

	EPS2= EPS*2

	DET = 1.0		!Se incializa el determinante

	DO 1010 I=1, N-1
		PV=I
		DO J=I+1, N
			IF (ABS(A(PV,I)) .LT. ABS(A(J,I))) PV=J
		END DO
		IF (PV .EQ. I) GOTO 1050
		DO JC=1, N+1
			TM=A(I,JC)
			A(I,JC)=A(PV,JC)
			A(PV,JC)=TM
		END DO

1045		DET=-1*DET   !Cada vez que se hace un pivoteo, cambia el signo de DET
1050		IF (A(I,I) .EQ. 0) GOTO 1200 	!La matriz es singular si A(I,I)= 0
		DO JR=I+1, N
			IF (A(JR,I) .NE. 0) THEN
				R=A(JR,I)/A(I,I)
				DO KC=I+1, N+1
					TEMP=A(JR,KC)
					A(JR,KC)=A(JR,KC)-R*A(I,KC)
					IF (ABS(A(JR,KC)) .LT. EPS2*TEMP) A(JR,KC)=0.0
!Si el resultado de la resta es menor que el doble del epsilon de la maquina por el
!valor original, se deja el valor de cero.
				END DO
			END IF
		END DO
1010	CONTINUE

	DO I=1, N
		DET=DET*A(I,I)
	END DO
	
	PRINT *
	PRINT *, 'DETERMINANTE = ', DET
	PRINT*

	IF (A(N,N) .EQ. 0) GOTO 1200
	A(N,N+1)=A(N,N+1)/A(N,N)
	DO NV=N-1, 1, -1		!Comienza la sustitución hacia atrás
		VA=A(NV,N+1)
		DO K=NV+1, N
			VA=VA-A(NV,K)*A(K,N+1)
		END DO
		A(NV,N+1)=VA/A(NV,NV)
	END DO
	RETURN

1200	PRINT *,'LA MATRIZ ES SINGULAR'
	END
		
